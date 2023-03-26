# lab-server

Server application responsible for providing clients with time-series data, comparing aggregated values

## Functionalities

- `/clients/handshake` endpoint which gives "handshake" functionality

- `/clients` endpoint to have an overview of available clients

- `/results` endpoint for comparing aggregated values

- `send_data()` function which start to send time-series data to clients on key press (does not work in Docker)

## How to run

- make yourself familiar with /app/constants.py content. Edit `DAY_SHIFT`, `REFRESH_INTERVAL`, `KEYBOARD_PRESS` if needed.

- `docker build -t lab-server .`

- `docker run -d --name lab-server -p 5670:5670 lab-server`

Alternatively install all needed packages and run server locally:

```
pip install -r requirements.txt

uvicorn app.main:app --port 5670
```

## Additional information

Visit `http://localhost:5670/redoc` to see docs
