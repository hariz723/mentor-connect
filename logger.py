import logging
import os
import time
from fastapi import Request # type: ignore
from logging.handlers import RotatingFileHandler

os.makedirs("logs", exist_ok=True)

# Configure logger
logger = logging.getLogger("App_Logger")
logger.setLevel(logging.INFO)

# File handler (rotate every 5MB, keep 3 backups)
file_handler = RotatingFileHandler("logs/app.log", maxBytes=5_000_000, backupCount=3)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add Handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)


async def log_requests(request: Request, call_next):
    """
    Middleware function to log details of incoming HTTP requests and their responses.

    Args:
        request (Request): The incoming HTTP request object.
        call_next (Callable): A callable to send the request to the next middleware or route handler.

    Returns:
        Response: The HTTP response generated after processing the request.

    The function logs the HTTP method and URL of the request upon receiving it, and logs the response status code
    and processing time upon sending the response. Logs unhandled exceptions with error details.
    """

    start_time = time.time()

    # Log request
    logger.info(f"➡️  {request.method} {request.url}")

    try:
        response = await call_next(request)
    except Exception as e:
        logger.error("Unhandled exception occurred", exc_info=True)
        raise e  # Let the exception handler manage the response

    process_time = (time.time() - start_time) * 1000
    logger.info(f"⬅️  {request.method} {request.url} - {response.status_code} ({process_time:.2f}ms)")

    return response