import asyncio
from aiogram import  Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import YOUR_TOKEN # Important: config.py is added to .gitignore to prevent token leakage.
                            

bot = Bot(token=YOUR_TOKEN) # Initialize the bot using the token from config.py.
dp = Dispatcher()


    
@db.message(CommandStart())
async def cmd_start(message:Message):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='one', callback_data="btn_one"),
                    InlineKeyboardButton(text='two', callback_data="btn_two"),
                    InlineKeyboardButton(text='three', callback_data="btn_three")
                ]
            ]
        )
        await message.answer(f"Hello", reply_markup=markup)

@db.callback_query(F.data=="btn_one")
async def handle_btn_one(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Button one")

@db.callback_query(F.data=="btn_two")
async def handle_btn_two(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Button two")

@db.callback_query(F.data=="btn_three")
async def handle_btn_three(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Button three")


async def main():
    await db.start_polling(bot) 

if __name__ == '__main__':
    asyncio.run(main())
