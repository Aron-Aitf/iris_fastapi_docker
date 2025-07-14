from duckdb import connect
from fastapi import FastAPI, HTTPException

DESCRIPTION = """
## A Data Science API that provides:

- ### The Iris Dataset (clean and raw)

- ### Low and High dimensional embeddings for the iris dataset

- ### A Iris Prediction Model (for both embeddings and normal)

"""

database = connect("./data/database.db", read_only=True)

app = FastAPI(
    swagger_ui_parameters = {"tryItOutEnabled": True},
    title = "Iris-API",
    debug = True,
    version = "0",
    description = DESCRIPTION.strip(),
)

@app.get("/")
def home():
    return {
        "title" : "Iris-API",
        "description" : DESCRIPTION,
        "description_type" : "markdown"
        }


@app.get("/get_data/split/{data_name}")
def get_iris_data(
    data_name : str
    ) -> list[dict[str, float]]:

    data_name = data_name.replace(" ", "_").lower()
    try:
        return database.sql(f"from {data_name}").pl().to_dicts()
    except:
        raise HTTPException(400, "invalid data name")