FROM python:3.13-bookworm 

WORKDIR /main

RUN pip install --no-cache-dir --upgrade pip 

RUN pip install --no-cache-dir polars
RUN pip install --no-cache-dir "fastapi[all]"
RUN pip install --no-cache-dir scikit-learn

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "./src/api/endpoints.py"]