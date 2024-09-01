from contextlib import asynccontextmanager

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


# Loguru
from backend.app.logger import logger


# Routers depends
from pages.router import router as router_pages


# Startup events
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('FastAPI is started')

    yield


# FastAPI initialize
app = FastAPI(
    lifespan=lifespan,
    title='C-Bank',
    redoc_url=None,
)

# Mount static files
app.mount('/static', StaticFiles(directory='static'), name='static')


# Files
# App Favicon
@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse('static/icons/favicon.ico')


# Routers
app.include_router(router_pages)


# CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=[
        'http://localhost',
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization',
    ],
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app, host='127.0.0.1', port=80, log_level='info', lifespan='on'
    )
