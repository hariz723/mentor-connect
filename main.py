'''
@author: Hari

source:
    ?
'''
from fastapi import FastAPI, Request

#local imports
from schemas import UserSchema
import constants as con
import auth

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/login')
async def login_get():
    pass


@app.post("/login")
async def login_post(
    request : Request,
    user : UserSchema
):
    username = user.username
    password = user.password
    

    if username == con.USERNAME and password == con.PASSWORD:
        return {
            "message" : "success",
            "token" : auth.create_access_token({"sub": username})
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8000
    )