import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from config import cache


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "старт",
        reply_markup=types.ReplyKeyboardRemove()
    )


async def cmd_reg(message: types.Message, state: FSMContext):
    await state.finish()
    await cache.set_data(chat=message.chat, user=message.from_user.id, data='зарегистрирован')
    await message.answer(
        "регистрация",
        reply_markup=types.ReplyKeyboardRemove()
    )


async def cmd_action(message: types.Message, state: FSMContext):
    await state.finish()
    data = await cache.get_data(chat=message.chat, user=message.from_user.id)
    await message.answer(data)
    await message.answer(
        "действие",
        reply_markup=types.ReplyKeyboardRemove()
    )


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())


async def check_registration(message: types.Message):
    reg = await cache.get_data(chat=message.chat, user=message.from_user.id)
    await message.answer(reg)
    if reg == "зарегистрирован":
        return True
    else:
        return False


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(
        cmd_start,
        lambda message: asyncio.create_task(check_registration(message)),
        commands="start",
        state="*")
    dp.register_message_handler(cmd_reg, commands="reg", state="*")
    dp.register_message_handler(cmd_action, commands="action", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
