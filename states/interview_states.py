from aiogram.fsm.state import StatesGroup, State

class InterviewState(StatesGroup):
    choosing_level = State()
    answering = State()