import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()
        response = await call_next(request)

        total_time = time.time() - start_time
        response.headers['X-Process-Time'] = f"{total_time:.5f}"
        # print(f"Request: {request.url.path} processed in {total_time:.5f} seconds")
        return response
