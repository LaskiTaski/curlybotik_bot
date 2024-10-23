from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMClient(StatesGroup):
    Start = State()
    Wait = State()
    SendMessage = State()
