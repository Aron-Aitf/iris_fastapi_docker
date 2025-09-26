from polars import read_csv, DataFrame
from sklearn.model_selection import train_test_split

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

for data_portion, name in zip([train_input, test_input, train_output, test_output], ["train_input", "test_input", "train_output", "test_output"]):
    data_portion.write_csv(f"./data/split_iris/{name}.csv")
