from datetime import datetime

# Loguru
from loguru import logger


def get_current_date():
    return datetime.now().strftime('%d-%m-%Y')


logger.add(
    f'logs/{get_current_date()}_C-Bask.log',
    rotation='00:00',
    retention='1 day',
    level='ERROR',
    format='{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}',
)

logger.add(
    f'logs/{get_current_date()}_C-Bask.log',
    rotation='00:00',
    retention='1 day',
    level='INFO',
    format='{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}',
)

logger.add(
    f'logs/{get_current_date()}_C-Bask.log',
    rotation='00:00',
    retention='1 day',
    level='WARNING',
    format='{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}',
)