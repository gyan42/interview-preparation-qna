import psycopg2
import time
import requests
import json


# Load the secrets
# secrets = hidden.secrets()

secrets = {"host": "pg.pg4e.com",
            "port": 5432,
            "database": "pg4e_757ed0c545",
            "user": "pg4e_757ed0c545",
            "pass": "pg4e_p_ed836428cb7aaa1"}

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)


cur = conn.cursor()

# response = requests.get(url)
# text = response.text
# print(json.loads(text))

sql = '''
DROP TABLE IF EXISTS pokeapi ;
'''
print(sql)
cur.execute(sql)

sql = '''
CREATE TABLE IF NOT EXISTS pokeapi
(id SERIAL, body JSONB);
'''
print(sql)
cur.execute(sql)


for i in range(100):
    url = f'https://pokeapi.co/api/v2/pokemon/{i+1}/'

    text = "None"
    try:
        print('=== Url is', url)
        response = requests.get(url)
        text = response.text
        print(text[:5])
        sql = 'INSERT INTO pokeapi (body) VALUES (%s::JSONB);'
        cur.execute(sql, ([text]))
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except Exception as e:
        print("Unable to retrieve or parse page", url)
        print("Error", e)
        continue

print('Closing database connection...')
conn.commit()
cur.close()



# defaulturl = 'https://pokeapi.co/api/v2/pokemon?limit=100&offset=0'
#
# response = requests.get(defaulturl)
# js = response.json() # <== THIS IS ONE OF THE CORRECTIONS, I NEEDED TO DE-
#                      #     SERIALIZE THE RESPONSE SO THAT IT'S A PROPER
#                      #     PYTHON DICTIONERY
#
# # js is a library and i'm interested in the values of 'results' key.
# results = js['results']
#
# # 'results' is a list of libraries and i want to loop through each element of the list
# # and extract the value of 'url' key
# # I NEED TO INSERT EACH VALUE INTO pokeapi (body), note that 'body' is of type JSONB
#
# for x in range(len(results)):
#     body = requests.get(results[x]['url'])
#     js_body = json.dumps(body) # <== 2ND MAJOR CORRECTION, I HAVE TO
#                                #     SERIALIZE THE PYTHON DICTIONERY/LIST
#                                #     TO BE ABLE TO CAST IT TO JSONB BELLOW
#     sql = f"INSERT INTO pokeapi (body) VALUES ('{js_body}'::JSONB)";
#     cur.execute(sql, (defaulturl))
#
# print('Closing database connection...')
# conn.commit()
# cur.close()