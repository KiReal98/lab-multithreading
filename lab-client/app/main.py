from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time

app = FastAPI()


class SensorDataEntry(BaseModel):
    data_type: str
    day: int
    val: float


class Handshake(BaseModel):
    ip_addr: str
    port: int


SERVER_IP = 'localhost'
SERVER_PORT = 5670

CLIENT_IP = 'localhost'
CLIENT_PORT = 6780


@app.post("/sensor-data", status_code=201)
async def create_sensor_data(sensor_data_entry: SensorDataEntry):
    if (sensor_data_entry.data_type == "KONIEC"):
        time.sleep(3)
        res = requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/results",
                            json={"ip_addr": CLIENT_IP, "port": CLIENT_PORT, "aggregates": [{"day": 0,  "HUM_MIN": 10, "HUM_MAX": 13, "HUM_MEAN": 12, "HUM_MEDIAN": 12,
                                                                                             "TEMP_MIN": 10, "TEMP_MAX": 13, "TEMP_MEAN": 12, "TEMP_MEDIAN": 12,
                                                                                             "LIGHT_MIN": 10, "LIGHT_MAX": 13, "LIGHT_MEAN": 12, "LIGHT_MEDIAN": 12,
                                                                                             "PRESS_MIN": 10, "PRESS_MAX": 13, "PRESS_MEAN": 12, "PRESS_MEDIAN": 12,
                                                                                             "PREC_MIN": 10, "PREC_MAX": 13, "PREC_MEAN": 12, "PREC_MEDIAN": 12, }]})


@app.post("/hello")
async def say_hello(payload: Handshake):
    res = requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/clients/handshake",
                        json={"ip_addr": payload.ip_addr, "port": payload.port})
    if (res.status_code == 201):
        return "Success"
    else:
        return f"Error occurred {res.text}"
