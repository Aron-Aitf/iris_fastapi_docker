from pickle import dump, HIGHEST_PROTOCOL
from polars import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

train_input = read_csv("./data/split_iris/train_input.csv")
train_output = read_csv("./data/split_iris/train_output.csv").to_series()


pipeline = make_pipeline(
    StandardScaler(), # all numerical features
    RandomForestClassifier(n_estimators=500)
)

pipeline.set_output(transform="polars") # type: ignore
pipeline.fit(train_input, train_output)


with open("./data/models/model.pkl", "wb") as file:
    dump(pipeline, file, HIGHEST_PROTOCOL)
    