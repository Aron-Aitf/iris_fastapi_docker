# Iris-API

## A Data Science API that provides:

- ### The Iris Dataset (cleaned and raw)

- ### A Iris Prediction Model

## Commands

- ### Build Image
```powershell
docker build -t ai-api .
```

- ### Run Image
```powershell
docker run -d -p 8000:8000 --name iris_api ai-api 
```
