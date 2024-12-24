import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
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

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Рассчитать норму калорий", callback_data="calories"
            ),
            InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
        ]
    ]
)


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью", reply_markup=start_kb
    )


@dp.message(F.text == "Рассчитать")
async def main_menu(message: Message) -> None:
    await message.answer("Выберите опцию:", reply_markup=menu_kb)


@dp.callback_query(F.data == "formulas")
async def get_formulas(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )


############################### FSM #############################
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.callback_query(StateFilter(None), F.data == "calories")
async def set_age(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def set_sex(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    await message.answer("Введите Ваш пол в формате М или Ж:")
    await state.set_state(UserState.sex)


@dp.message(UserState.sex)
async def send_calories(message: Message, state: FSMContext) -> None:
    await state.update_data(sex=message.text.lower())
    data = await state.get_data()
    if data["sex"] in ("м", "m", "мужской", "man"):
        calorie_intake = (
            10 * int(data["weight"])
            + 6.25 * int(data["growth"])
            - 5 * int(data["age"])
            + 5
        )
        await message.answer(f"Ваша норма калорий: {calorie_intake}")
    elif data["sex"] in ("ж", "w", "женский", "woman"):
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
