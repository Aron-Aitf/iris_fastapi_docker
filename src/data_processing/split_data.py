from pickle import dump, HIGHEST_PROTOCOL
from polars import read_csv, DataFrame

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import KNNImputer
from sklearn.preprocessing import (
    StandardScaler,
    FunctionTransformer
)

data = read_csv("./data/cleaned_iris.csv")

input_data = data.drop("species")
output_data = data.select("species")

train_percentage = 80

split_data : tuple[DataFrame, DataFrame, DataFrame, DataFrame] = tuple(
    train_test_split
    (
        input_data,
        output_data,
        train_size=train_percentage/100
    )
)

train_input, test_input, train_output, test_output = split_data


preprocessing_pipeline = make_pipeline(
    KNNImputer(n_neighbors=2), # just for completeness (iris has no null values)
    StandardScaler(), # all numerical features
)


preprocessing_pipeline.set_output(transform="polars") # type: ignore

train_input : DataFrame = preprocessing_pipeline.fit_transform(train_input) # type: ignore
test_input : DataFrame = preprocessing_pipeline.transform(test_input) # type: ignore

with open("data/models/preprocessing_pipeline.pkl", "wb") as file:
    dump(preprocessing_pipeline, file, HIGHEST_PROTOCOL)


for data_portion, name in zip([train_input, test_input, train_output, test_output], ["train_input", "test_input", "train_output", "test_output"]):
    data_portion.write_csv(f"./data/split_iris/{name}.csv")
