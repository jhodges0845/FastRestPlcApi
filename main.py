from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/plc/read/{data_type}/{tag_value}")
def read_plc(tag_value: str, data_type: str):
    return {"tag_value": tag_value, "data_type": data_type}
