from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import asyncio 
from service import makeresponse
from conf import BOT_TOKEN


async def main():
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    @dp.message(F.text)
    async def start(message: Message):
        await message.answer(makeresponse(message))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    print("Bot started")
