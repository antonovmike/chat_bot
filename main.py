import asyncio
import datetime
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart

from openai import OpenAI

from dotenv import load_dotenv

import db


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
router = Router()
client = OpenAI(api_key=os.getenv('GPT'))


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer_sticker('CAACAgIAAxkBAAIUSWWalI3UK4cUW2s25m49M2WlW6SZAAI7AQACijc4AAGSEIzViMEnBDQE')
    await message.answer(f'Hello {message.from_user.full_name}')
    db.add_user(
        telegram_id=str(message.from_user.id),
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Who won the world series in 2020?"
        },
    ]
)

print(response.choices)


@dp.message()
async def echo(message: types.Message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message.text
            },
        ]
    )
    # Get message from ChatGPT
    answer = response.choices[0].message.content.strip()
    # Send ChatGPT message to Telegram
    await message.answer(answer)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    db.create_table()
    asyncio.run(main())
