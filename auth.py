'''
@author: Hari

source:
    ?
'''

from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer


#local imports
import constants as const

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=const.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": data, "exp": expire}
    return jwt.encode(payload, const.SECRET_KEY, algorithm=const.ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, const.SECRET_KEY, algorithms=[const.ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="INVALID CREDENTIALS")