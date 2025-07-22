import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import YOUR_TOKEN # Important: config.py is added to .gitignore to prevent token leakage.
                            

bot = Bot(token=YOUR_TOKEN) # Initialize the bot using the token from config.py.
db = Dispatcher()


@db.message(CommandStart())
async def cmd_start(message:Message):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='???', callback_data="?"),
                    InlineKeyboardButton(text='???', callback_data="?"),
                    InlineKeyboardButton(text='???', callback_data="?")
                ]
            ]
        )
        await message.answer(f"Hello", reply_markup=markup)


async def main():
    await db.start_polling(bot) 

if __name__ == '__main__':
    asyncio.run(main())
    print("bot start")