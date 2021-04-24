from fastapi import FastAPI
from PlcInterface.interface import read_plc, write_plc

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/plc/read/{ip_address}/{tag_name}")
def plc_read(ip_address: str, tag_name):
    #read from PLC#
    data = read_plc(ip_address, tag_name)

    return data
