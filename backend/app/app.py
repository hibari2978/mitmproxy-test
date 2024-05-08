from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Authentication(BaseModel):
    password: str
    
class Privilege(BaseModel):
    name: str

@app.post("/auth")
async def auth(authentication : Authentication):
    privilege: Privilege = Privilege(name="none")
    
    if authentication.password == "A":
        privilege.name = "admin"
    elif authentication.password == "B":
        privilege.name = "user"
    
    return privilege