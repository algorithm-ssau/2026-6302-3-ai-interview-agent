# Новая структура: тема → уровень → список вопросов (по 2 вопроса для теста)
QUESTIONS = {
    "Python": {
        "Junior": [
            "Что такое PEP8?",
            "Чем отличается list от tuple?"
        ],
        "Middle": [
            "Как работает сборщик мусора в Python?",
            "Что такое asyncio?"
        ],
        "Senior": [
            "Как устроен интерпретатор CPython?",
            "Что такое GIL-free Python?"
        ]
    },
    "Java": {
        "Junior": [
            "Что такое JVM?",
            "Чем отличается `==` от `equals()`?"
        ],
        "Middle": [
            "Как работает сборщик мусора в Java?",
            "Что такое Stream API?"
        ],
        "Senior": [
            "Как работает загрузка классов в Java?",
            "Что такое Java Memory Model?"
        ]
    },
    "SQL": {
        "Junior": [
            "Что такое JOIN?",
            "Чем отличается INNER JOIN от LEFT JOIN?"
        ],
        "Middle": [
            "Что такое транзакции и ACID?",
            "Что такое оконные функции?"
        ],
        "Senior": [
            "Что такое шардирование и партиционирование?",
            "Что такое CAP теорема?"
        ]
    },
    "Git": {
        "Junior": [
            "Что такое Git?",
            "Чем отличается git pull от git fetch?"
        ],
        "Middle": [
            "Чем отличается rebase от merge?",
            "Что такое cherry-pick?"
        ],
        "Senior": [
            "Как настроить CI/CD с Git?",
            "Что такое Git hooks?"
        ]
    }
}

def get_topics():
    """Возвращает список доступных тем"""
    return list(QUESTIONS.keys())

def get_levels_for_topic(topic: str):
    """Возвращает список уровней для темы"""
    return list(QUESTIONS.get(topic, {}).keys())

def get_questions(topic: str, level: str):
    """Возвращает вопросы для темы и уровня"""
    return QUESTIONS.get(topic, {}).get(level, [])

def get_next_question(questions: list, index: int):
    """Возвращает следующий вопрос по индексу"""
    return questions[index] if index < len(questions) else None