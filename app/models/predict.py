from pydantic import BaseModel

#Input and Output pydantic models inherting Basemodel 


class Input(BaseModel):
    text: str


class Output(BaseModel):
    language: str

    
