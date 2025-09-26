from pickle import load
from sklearn.pipeline import Pipeline
from polars import read_csv

with open("./data/models/model.pkl", "rb") as file:
    model : Pipeline = load(file)

test_input = read_csv("data/split_iris/test_input.csv")
test_output = read_csv("data/split_iris/test_output.csv")

print(model.score(test_input, test_output))