FROM python:3.13-bookworm 

WORKDIR /main

RUN pip install --no-cache-dir --upgrade pip 

RUN pip install --no-cache-dir polars
RUN pip install --no-cache-dir "fastapi[all]"
RUN pip install --no-cache-dir scikit-learn
RUN pip install --no-cache-dir gunicorn

COPY . .

RUN python3 ./src/data_processing/clean_data.py
RUN python3 ./src/data_processing/split_data.py
RUN python3 ./src/machine_learning/model.py


CMD ["gunicorn", "-w", "17", "-k", "uvicorn.workers.UvicornWorker", "src.api.endpoints:app", "--bind", "0.0.0.0:8000", "--forwarded-allow-ips", "*"]