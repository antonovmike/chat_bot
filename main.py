import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
router = Router()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f'Hello {message.from_user.full_name}')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
