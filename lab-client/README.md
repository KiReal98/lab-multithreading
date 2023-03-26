# lab-client

Client application for gathering time-series data

## Functionalities

- `/hello` endpoint, which allows "handshake" with server application

- `/sensor-data` endpoint for gathering time series data

## How to run

- in /app/main.py set the following values (default values can be used when running both client and server locally not in Docker!):

```
   SERVER_IP = 'localhost'
   SERVER_PORT = 5670

   CLIENT_IP = 'localhost'
   CLIENT_PORT = 6780
```

- `docker build -t lab-client .`

- `docker run -d --name lab-client -p 6780:6780 lab-client`

Alternatively install all needed packages and run server locally:

```
pip install -r requirements.txt

uvicorn app.main:app --port 6780
```

## Additional information

Visit `http://localhost:6780/redoc` to see docs
