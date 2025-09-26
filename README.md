# A Data Science API

## This was a old project to learn APIs and data science

## This was repurposed as a project to learn networking and API deployment

## More information cam be found in the swagger UI docs at <http://localhost:80/docs> when the API is running on the computer

## Running

### To run, The only requirement is Docker Compose  

#### Run

```bash
docker compose up --build -d
```

#### Show Output

```bash
docker compose logs -f
```

#### Stop

```bash
docker compose down --volumes
```

## How it works

### This project uses Docker Compose to manage containers and Nginx as a reverse proxy

#### Nginx is used as a reverse proxy to Fastapi while handling rate limiting and caching

#### Docker and Docker compose are used to manage both the API and Nginx in separate containers while restarting them if they crash
