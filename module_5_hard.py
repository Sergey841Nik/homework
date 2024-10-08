
from time import sleep
from typing import Any

class Users:
    def __init__(self, name: str, password: Any, age: int) -> None:
        self.name = name
        self.password = hash(password)
        self.age = age
        self.valid(password)

    def valid(self, password):
        if not (isinstance(self.name, str) and isinstance(self.age, int)):
            raise TypeError("Неверный формат введённых данных")
        elif len(password) < 8:
            raise ValueError("Пароль слишком короткий")
        
class Video:
    def __init__(self, title: str, 
                 duration: int, 
                 time_now: int=0, 
                 adult_mode: bool=False
                 ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.valid()

    def valid(self):
        if not (isinstance(self.title, str) and isinstance(self.duration, int)):
            raise TypeError("Неверный формат введённых данных")
        

class UrTube:
    users_lst = []
    videos_lst = []

    def __init__(self):
        self.current_user=None
    
    def register(self, name: str, password: str, age: int):
        user = Users(name, password, age)
        for user in self.users_lst:
            if user.name == name:
                print(f"Пользователь с именем {name} уже зарегистрирован")
                return
        self.users_lst.append(user)
        print("Вы успешно зарегистрировались")
    
    def log_in(self, name: str, password: str):
        for user in self.users_lst:
            if user.name == name and user.password == hash(password):
                self.current_user = user.name
                print('Вы успешно авторизировались')
                return
        print(f"Пользователь с именем {name} не зарегистрирован")
    
    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add_video(self, *args):
        if self.current_user:
            for arg in args:
                self.videos_lst.append(arg)
            print("Вы добавили видео")
        else:
            print("Вы не авторизированы")

    def get_video(self, title: str):
        steck = []
        for video in self.videos_lst:
            if title.lower() in video.title.lower():
                steck.append(video.title)
        return ",".join(steck)
    
    def watch_video(self, title: str):
        if  self.current_user:
            steck = []
            for video in self.videos_lst:
                if title == video.title:
                    steck.append(video.time_now)
                    steck.append(video.duration)
                    steck.append(video.adult_mode)
            if not steck:
                print("Видео не найдено")
            else:
                for user in self.users_lst:
                    if self.current_user == user.name:
                        steck.append(user.age)
                if steck[2] and steck[-1] < 18:
                    print("Ай. 18 лет нет ещё")
                else: 
                    for t in range(steck[0], steck[1]+1):
                        print(t, end=" ")
                        sleep(0.1)
                    print("Конец видео")
        else:
            print("Эх, вы не авторизированы")
    
    
us1 = UrTube()
us2 = UrTube()
us1.register("Иван", "123456789", 20)
us2.register("Петр", "987654321", 12)
us1.log_in("Иван", "123456789")
v1 = Video("Не та дверь", 12, adult_mode=True)
v2 = Video("Синий трактор", 10)
v3 = Video("Лунтик", 10)
us1.add_video(v1, v2)
us2.add_video(v3)
us2.log_in("Петр", "987654321")
print(us1.get_video("ДвеР"))
us1.watch_video("Не та дверь")
us2.watch_video("Не та дверь")
us1.log_out()
us2.watch_video("Синий трактор")
us3 = UrTube()
us3.log_in('Гешка', 12365789)

