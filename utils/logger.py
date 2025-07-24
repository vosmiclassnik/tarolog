import logging
import os


def setup_logger(name='tarolog'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Создаём директорию для логов, если её нет
    os.makedirs('logs', exist_ok=True)

    # Файл логов
    file_handler = logging.FileHandler('logs/bot.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Формат логов
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавляем хендлеры, если ещё не добавлены
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger