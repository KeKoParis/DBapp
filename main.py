from loguru import logger

from database import DB

#logger.remove()
logger.add("program.log", format="{time} {level} {message}", level="INFO")

