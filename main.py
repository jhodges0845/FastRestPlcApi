from fastapi import FastAPI
from PlcInterface.interface import read_plc, write_plc, info_plc, read_all_plc
from Networking.networking import Ping

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

#Network Routes

@app.get("/ping/{ip_address}")
def ping(ip_address: str):
    data = Ping(ip_address)
    return {"data": data}


# PLC Routes

@app.get("/plc/read/{ip_address}/{tag_name}")
def plc_read(ip_address: str, tag_name):
    #read from PLC#
    data = read_plc(ip_address, tag_name)

    return {"data": data}

@app.get("/plc/write/{ip_address}/{tag_name}/{data_type}/{tag_value}")
def plc_write(ip_address: str, tag_name: str, data_type: str, tag_value):
    # Validate tag value with data type #
    
    # write value to PLC #
    data = write_plc(ip_address, tag_name, tag_value)

    return {"data": data}

@app.get("/plc/info/{ip_address}")
def plc_info(ip_address: str):
    #Get Version of PLC
    data = info_plc(ip_address)

    return {"data": data}

@app.get("/plc/read/all/{ip_address}")
def plc_tagInfo(ip_address: str):

    #Get All Tags of PLC
    data = read_all_plc(ip_address)

    return {"data": data}


