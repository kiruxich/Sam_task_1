from typing import Dict, Any, Set

from fastapi import FastAPI
from users import *

app = FastAPI()


@app.post("/register/")
def register_user(first_name, second_name, age, email):
    sending(first_name, second_name, age, email)
    return "ВСЕ ЗАЕБИСЬ"


@app.get("/users/{id}")
def data_getting(id: int) -> dict[str, Any] | set[str]:
    try:
        data = polychenie(id)
        return {"id": data[0][0], "Имя:": data[0][1], "Фамилия": data[0][2], "Возраст": data[0][3], "Почта": data[0][4]}

    except:
        return {"Нет пользователя с таким id"}

#/register/?first_name=один&second_name=два&age=3&email=четыре

print('хуй')


