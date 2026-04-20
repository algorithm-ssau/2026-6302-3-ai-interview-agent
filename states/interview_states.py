from aiogram.fsm.state import StatesGroup, State

class InterviewState(StatesGroup):
    choosing_topic = State()
    choosing_level = State()
    answering = State()