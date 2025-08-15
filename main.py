'''
@author: Hari

source:
    ?
'''
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

#local imports
import constants as con
import token
from src.schemas import (
    UserSchema,
    SuccessResponse,
    ErrorResponse
)
from logger import log_requests, logger

app = FastAPI()

app.middleware("http")(log_requests)

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
    
    try: 
        username = user.username
        password = user.password
        

        if username == con.USERNAME and password == con.PASSWORD:
            token = token.create_access_token(user.dict())
            response = RedirectResponse(url='/login', status_code=302)
            response.set_cookie(key = "access_token", value = token)
            return SuccessResponse(
                message = "Login Successful",
                status_code = 200,
                data = {response}
            )
            
    except Exception as e:
        return ErrorResponse(
            message = "Invalid Credentials",
            status_code = 401,
            error_message = {"Error": str(e)}
        )





if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        reload=True,
        port=8000
    )
