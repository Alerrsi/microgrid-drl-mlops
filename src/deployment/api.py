from fastapi import FastAPI

# aplicación principal
app = FastAPI()


@app.post("apiv1/send/")
async def send(Soc, demand, hour):
    return {}
