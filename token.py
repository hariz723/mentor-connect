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
    """
    Create a JWT access token for the given data.

    Args:
        data (dict): The data to include in the token payload, typically user information.

    Returns:
        str: The encoded JWT access token.

    The token will contain the provided data in its payload and an expiration time
    set to the current time plus a predefined number of minutes. The token is signed
    using a secret key and a specified algorithm.
    """

    expire: datetime = datetime.now() + timedelta(minutes=const.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload: dict[str, datetime] = {"sub": data.dict(), "exp": expire} # type: ignore
    return jwt.encode(payload, const.SECRET_KEY, algorithm=const.ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieve the current user from the provided JWT access token.

    Args:
        token (str): The JWT access token to authenticate with.

    Returns:
        str: The username of the authenticated user.

    Raises:
        HTTPException: If the provided token is invalid, expired, or otherwise
            invalid.

    The function will attempt to decode the JWT token using the secret key and
    algorithm specified in the constants module. If successful, it will return
    the username from the token payload. Otherwise, it will raise an HTTPException
    with a status code of 401 and a detail message of "INVALID CREDENTIALS".
    """
    try:
        payload = jwt.decode(token, const.SECRET_KEY, algorithms=[const.ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="INVALID CREDENTIALS")
