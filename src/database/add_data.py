from duckdb import connect
from os import getcwd

database = connect("./data/database.db")

tables = {
    "raw_iris" : "data/iris.csv",
    "cleaned_iris" : "data/cleaned_iris.csv",
    "test_input" : "data/split_iris/test_input.csv",
    "test_output" : "data/split_iris/test_output.csv",
    "train_input" : "data/split_iris/train_input.csv",
    "train_output" : "data/split_iris/train_output.csv"
}

for table_name, csv_path in tables.items():
    full_path = (f"{getcwd()}/{csv_path}").replace("\\", "/")
    sql = f"create or replace table {table_name} as from '{full_path}'"
    database.sql(sql)

database.close()
