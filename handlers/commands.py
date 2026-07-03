from loader import dp
from states import State
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
import broadcast


@dp.message_handler(commands=['broad_casttt'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await broadcast.main()

@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    print(message)
    await message.answer(texts.help)

@dp.message_handler(commands=['terms'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('terms.pdf', 'rb') as f:
        await message.answer_document(f)


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/Max.jpeg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t1)
    with open("01_Согласие_на_обработку_персональных_данных.pdf", "rb") as file:
        await message.answer_document(file, caption=texts.terms_caption, reply_markup=kb.terms_accepted)
    # await message.answer(texts.t2)
    await State.terms.set()
    # await State.enter_name.set()



@dp.callback_query_handler(state=State.terms)
async def agree_callback(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer(texts.t2)
    await State.enter_name.set()