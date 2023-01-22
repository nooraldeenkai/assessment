from pydantic import BaseModel
import datetime


#
class Input(BaseModel):
    text: str


class Output(BaseModel):
    language: str

    