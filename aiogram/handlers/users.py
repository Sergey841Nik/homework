from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from kbbtn.reply import get_kyboard

user_router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


# создаём клавиатуру функцией get_kyboard (попытался сделать универсальной)
USER_BTN = get_kyboard("Рассчитать", "Информация", placeholder="Что хотите сделать?")


@user_router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью", reply_markup=USER_BTN
    )


###############################FSM#############################
@user_router.message(StateFilter(None), F.text == "Рассчитать")
async def set_age(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove() #удаляем клавиатуру
    )
    await state.set_state(UserState.age)


@user_router.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


@user_router.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


@user_router.message(UserState.weight)
async def set_sex(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer("Введите Ваш пол в формате М или Ж:")
    await state.set_state(UserState.sex)


@user_router.message(UserState.sex)
async def send_calories(message: types.Message, state: FSMContext):
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
