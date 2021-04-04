from collections import defaultdict
input_data = ["3", "paris tokyo 9471", "paris new-york 5545", "new-york singapore 15344"]

graph = defaultdict(dict)
num_vertices = int(input_data[0])

for i in range(1, num_vertices+1):
  u,v,w = input_data[i].split()
  graph[u][v] = w
  # graph[v][u] = w

if __name__ == "__main__":
    print(graph)