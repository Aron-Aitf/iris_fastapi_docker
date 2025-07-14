from typing import Literal
from duckdb import connect
from fastapi import FastAPI, HTTPException
from pickle import load
from sklearn.pipeline import Pipeline
from polars import from_dicts

DESCRIPTION = """
## A Data Science API that provides:

- ### The Iris Dataset (clean and raw)

- ### Low and High dimensional embeddings for the iris dataset

- ### A Iris Prediction Model (for both embeddings and normal)

"""
with open("data/models/model.pkl", "rb") as file:
    model : Pipeline = load(file)

database = connect("./data/database.db", read_only=True)

app = FastAPI(
    swagger_ui_parameters = {"tryItOutEnabled": True},
    title = "Iris-API",
    debug = True,
    version = "0",
    description = DESCRIPTION.strip(),
)

@app.get("/")
def home() -> dict[str, str]:
    return {
        "title" : "Iris-API",
        "description" : DESCRIPTION,
        "description_type" : "markdown"
        }


@app.get("/get_data/split/{split_type}/{data_part}")
def get_iris_data(
    split_type : Literal["train", "test"],
    data_part : Literal["input", "output"]
    ) -> list[dict]:

    data_name = f"{split_type}_{data_part}"
    try:
        return database.sql(f"from {data_name}").pl().to_dicts()
    except:
        raise HTTPException(400, f"invalid parameters {split_type}, {data_part}")

@app.get("/get_data/whole/{data_type}")
def get_whole_iris(data_type : Literal["raw", "cleaned"]):
    try:
        return database.sql(f"from {data_type}_iris").pl().to_dicts()
    except:
        raise HTTPException(400, "invalid data_type")

@app.post("/model/predict/from_raw")
def raw_predict_iris(data : list[dict]) -> list[int]:
    try:
        return list(model.predict(from_dicts(data)))
    except:
        raise HTTPException(400, f"invalid data")

