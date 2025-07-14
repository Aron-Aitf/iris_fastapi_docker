from pickle import load, dump, HIGHEST_PROTOCOL
from polars import read_csv
from sklearn.ensemble import RandomTreesEmbedding, RandomForestClassifier
from sklearn.pipeline import make_pipeline

train_input = read_csv("data/split_iris/train_input.csv")
train_output = read_csv("data/split_iris/train_output.csv").to_series()

with open("data/models/preprocessing_pipeline.pkl", "rb") as file:
    data_preprocessor = load(file)


pipeline = make_pipeline(
    data_preprocessor,
    RandomTreesEmbedding(),
    RandomForestClassifier(n_estimators=500)
)

pipeline.fit(train_input, train_output)


print(pipeline.predict(train_input))

with open("data/models/model.pkl", "wb") as file:
    dump(pipeline, file, HIGHEST_PROTOCOL)