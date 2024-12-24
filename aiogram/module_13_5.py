import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

dp = Dispatcher()

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует",
)


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью", reply_markup=start_kb
    )


###############################FSM#############################
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message(StateFilter(None), F.text == "Рассчитать")
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def set_sex(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer("Введите Ваш пол в формате М или Ж:")
    await state.set_state(UserState.sex)


@dp.message(UserState.sex)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(sex=message.text.lower())
    data = await state.get_data()
    if data["sex"] == "м":
        calorie_intake = (
            10 * int(data["weight"])
            + 6.25 * int(data["growth"])
            - 5 * int(data["age"])
            + 5
        )
        await message.answer(f"Ваша норма калорий: {calorie_intake}")
    elif data["sex"] == "ж":
        calorie_intake = (
            10 * int(data["weight"])
            + 6.25 * int(data["growth"])
            - 5 * int(data["age"])
            - 161
        )
        await message.answer(f"Ваша норма калорий: {calorie_intake}")
    else:
        await message.answer(
            "Похоже Вы ввели неверно свой пол. Начните заново введите /start"
        )

    await state.clear()

@dp.message()
async def all_massages(message: Message) -> None:
    await message.answer("Введите команду /start, чтобы начать общение.")



async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
