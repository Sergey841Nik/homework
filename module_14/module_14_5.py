import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    BufferedInputFile
)
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from dotenv import find_dotenv, load_dotenv

from crud_functions import get_all_products, add_user, is_included

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
        [
            KeyboardButton(text="Купить"),
            KeyboardButton(text="Регистрация"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует",
)


# Функция  для создания инлайн клавиатур
def get_user_inline_btns(*, btns: dict[str, str], sizes: tuple[int]) -> InlineKeyboardMarkup:
    """
   Функция создает инлайн-клавиатуру для пользователя.
   Args:
       btns (dict[str, str]): Словарь, где ключ - текст кнопки, а значение - callback_data.
       sizes (tuple[int]): Кортеж, определяющий размеры кнопок.
   Returns:
       InlineKeyboardMarkup: Строка, представляющая инлайн-клавиатуру.
   """
    keyboard = InlineKeyboardBuilder()

    for text, callback_data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=callback_data))

    return keyboard.adjust(*sizes).as_markup()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью", reply_markup=start_kb
    )


@dp.message(F.text == "Рассчитать")
async def main_menu(message: Message) -> None:
    btns = {"Рассчитать норму калорий": "calories", "Формулы расчёта": "formulas"}
    await message.answer(
        "Выберите опцию:", reply_markup=get_user_inline_btns(btns=btns, sizes=(2,))
    )


@dp.message(F.text == "Купить")
async def get_buying_list(message: Message) -> None:
    btns = {}

    for product in get_all_products():
        btns[product[0]] = "product_buying"
        img = BufferedInputFile(product[3], "_.jpg")
        await message.answer_photo(
            img,
            caption=f"Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}",
        )
    await message.answer(
        "Выберите продукт для покупки:",
        reply_markup=get_user_inline_btns(btns=btns, sizes=(4,)),
    )


@dp.callback_query(F.data == "formulas")
async def get_formulas(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )


@dp.callback_query(F.data == "product_buying")
async def send_confirm_message(callback: CallbackQuery) -> None:
    await callback.message.answer("Вы успешно приобрели продукт!")

############################## FSM добавление пользователя #############################
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
 

@dp.message(StateFilter(None), F.text == "Регистрация")
async def sing_up(message: Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        
        return await state.set_state(RegistrationState.username)
    
    await state.update_data(username=message.text)
    await message.answer("Введите свой email:")
    await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age_for_reg_user(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data["username"], data["email"], data["age"])
    await message.answer("Регистрация прошла успешно")
    await state.clear()

############################### FSM расчёт калорий #############################
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
