import uvicorn
from fastapi import FastAPI

from app.api import router
from app.config import API_HOST, API_PORT, API_PREFIX


app = FastAPI(
    title="Link shortening service",
    debug=False,
    openapi_url=f"{API_PREFIX}/openapi.json",
)
app.include_router(router, prefix=API_PREFIX)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)
