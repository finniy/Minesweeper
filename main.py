import asyncio
from app.bot import main
# from app.logger import logger

# Запуск всей программы
if __name__ == "__main__":
    # logger.info("Запуск бота")
    asyncio.run(main())
