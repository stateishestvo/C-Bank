# FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# Loguru
from logger import logger


router = APIRouter(tags=['Pages'])
templates = Jinja2Templates(directory='templates')


# Root page
@router.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        return templates.TemplateResponse('pages/index.html', {'request': request})

    except Exception as e:
        logger.error(f'Error loading index.html: {e}')
        return templates.TemplateResponse('pages/error.html', {'request': request})

@router.get('/about', response_class=HTMLResponse)
async def go_about(request: Request):
    try:
        return templates.TemplateResponse('pages/about.html', {'request': request})

    except Exception as e:
        logger.error(f'Error loading index.html: {e}')
        return templates.TemplateResponse('pages/error.html', {'request': request})
    
@router.get('/news', response_class=HTMLResponse)
async def go_news(request: Request):
    try:
        return templates.TemplateResponse('pages/news.html', {'request': request})

    except Exception as e:
        logger.error(f'Error loading index.html: {e}')
        return templates.TemplateResponse('pages/error.html', {'request': request})

@router.get('/calculator', response_class=HTMLResponse)
async def go_calculator(request: Request):
    try:
        return templates.TemplateResponse('pages/calculator.html', {'request': request})

    except Exception as e:
        logger.error(f'Error loading index.html: {e}')
        return templates.TemplateResponse('pages/error.html', {'request': request})
    
@router.get('/index', response_class=HTMLResponse)
async def go_calculator(request: Request):
    try:
        return templates.TemplateResponse('pages/index.html', {'request': request})

    except Exception as e:
        logger.error(f'Error loading index.html: {e}')
        return templates.TemplateResponse('pages/error.html', {'request': request})