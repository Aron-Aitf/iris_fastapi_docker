FROM python:3.13-slim-bookworm 

WORKDIR /main

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir polars "fastapi[standard]" scikit-learn gunicorn

COPY . .

RUN python3 ./src/data_processing/clean_data.py && python3 ./src/data_processing/split_data.py && python3 ./src/machine_learning/model.py

CMD ["gunicorn", "-w", "17", "-k", "uvicorn.workers.UvicornWorker", "src.api.endpoints:app", "--bind", "0.0.0.0:8000", "--forwarded-allow-ips", "*"]