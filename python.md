# Python

- What is the difference between is and == ? is is for address comparison and == is for value comparison
    - Use is only to compare None!
    ```
    e=10;d=10; print(d == e, d is e)
    True True
    e=10**3;d=10**3; print(d == e, d is e)
    True False
    ```
- Can you explain Python dict implementation?
    - https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
    - So in summary, if there are two keys, a and b and hash(a)==hash(b), but a!=b, then both can exist harmoniously in a Python dict. But if hash(a)==hash(b) and a==b, then they cannot both be in the same dict. 
    - In short, dict is backed by hash tables. key’s hash value is used as the table index. On the event of hash collision along with key’s hash value, the key itself checked against breaking the collision and a new slot is decided randomly from available slots
    - Types (collections)
    - OrderedDict
    - Defaultdict
    - ChainMap
    - types.MappingProxyType ReadOnly
- dataclass.dataclass
    - ```
        @dataclass
        class DataClassCard:
        rank: str
        suit: str
      ```