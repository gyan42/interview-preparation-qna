# Airflow

- What is a DAG?
    - ETL workflow computations are marked as a node in a graph and the nodes are connected based on the dependency between the tasks. The graph is referred to as “DAGs” (Directed Acyclic Graphs).
- Define Sensor, Operators and Transfers?
    - Sensors: waits for a certain time, external file, or upstream data source
    - Operators: triggers a certain action (e.g. run a bash command, execute a python function, or execute a Hive query, etc)
    - Transfers: moves data from one location to another
