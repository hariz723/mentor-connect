from dotenv import load_dotenv
import os
from typing import TypeVar

T = TypeVar("T", str, int, float, bool)

load_dotenv()


def get_env(key: str, cast: type[T], default) -> bool | T  : 
    
    val = os.getenv(key, default)
    
    if val is None:
        return default
    
    if cast in {str, int, float}:
        return cast(val)
    elif cast is bool:
        return val.lower() in {"true", "1", "yes", "y"}
    else:
        raise ValueError(f"Invalid cast type: {cast}")
    
    
class ConfigLoader: 
    
    
    database_url = get_env("DATABASE_URL", cast=str, default="sqlite:///data.db")
    
    
    
settings = ConfigLoader()