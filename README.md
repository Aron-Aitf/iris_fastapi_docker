## A Data Science API that provides:

- ### The Iris Dataset (cleaned and raw)

- ### Iris Data Scaler

- ### A Iris Prediction Model (from scaled and raw)


## Commands

- ### Build Image
```powershell
docker build -t ai-api .
```

- ### Run Image
```powershell
docker run -d -p 8000:8000 --name iris_api ai-api 
```

- ### Run Normally
```powershell
fastapi run src\api\endpoints.py
```