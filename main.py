from fastapi import FastAPI, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class HostParams:
    def __init__(self,
                 localtion: str = None,
                 datFrom: str = None,

                 ) -> None:
        self.localtion = localtion
        self.datFrom = datFrom
        

@app.get("/host")
def getHost(serhArg: HostParams = Depends()
            ):
    return serhArg

class SModelParam (BaseModel):
    id:int
    value: str

app.post("/host")
def setParam (param:SModelParam):
    pass