from typing import Literal
from fastapi import FastAPI, HTTPException
from polars import read_csv, from_dicts
from pickle import load
from sklearn.pipeline import Pipeline

DESCRIPTION = """
## A Data Science API that provides:

- ### The Iris Dataset (cleaned and raw)

- ### A Iris Prediction Model

"""

app = FastAPI(
    swagger_ui_parameters = {"tryItOutEnabled": True},
    title = "Iris-API",
    debug = True,
    version = "0",
    description = DESCRIPTION.strip(),
)

with open("data/models/model.pkl", "rb") as file:
    model : Pipeline = load(file)

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

    try:
        return read_csv(f"data/split_iris/{split_type}_{data_part}.csv").to_dicts()
    except:
        raise HTTPException(400, "invalid parameters {split_type}, {data_part}")

@app.get("/get_data/whole/{data_type}")
def get_whole_iris(data_type : Literal["raw", "cleaned"]):
    try:
        path = f"data/{"" if data_type == "raw" else "cleaned_"}iris.csv"
        return read_csv(path).to_dicts()
    except Exception:
        raise HTTPException(400, "invalid data_type")

@app.post("/model/predict/from_raw")
def raw_predict_iris(data : list[dict]) -> list[int]:
    try:
        return list(model.predict(from_dicts(data)))
    except:
        raise HTTPException(400, "invalid data")

