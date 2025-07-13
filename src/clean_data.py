from polars import scan_csv, col

species_map = {
    "setosa" : 0,
    "versicolor" : 1,
    "virginica" : 2
}

(
    scan_csv("./src/data/iris.csv")
    .with_columns
    (
        col("species")
        .replace(species_map)
        .alias("species")
    )
    .sink_csv("./src/data/cleaned_iris.csv")
)

