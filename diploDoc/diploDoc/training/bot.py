# pip install -U aiogram
# pip install environs


import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token="7175352991:AAEsJ7VRKrzzsu6qy79kuSJkeVakLM2yrkE")
    dp = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    input()
if __name__ == '__main__':
    asyncio.run(main())

asyncio.run(main())