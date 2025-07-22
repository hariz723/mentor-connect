'''
@author: Hari

source:
    ?
'''
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

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
        token = auth.create_access_token(user)
        response = RedirectResponse(url='/login', status_code=302)
        response.set_cookie(key = "access_token", value = token)
        return response
    return {
        "status_code": 401,
        "message"    : "Invalid credentials"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        reload=True,
        port=8000
    )