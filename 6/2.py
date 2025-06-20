class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
users = [
    User("admin", "admin"),
    User("ivan", "qwerty"),
    User("stasik", "standoff2"),
    User("anna", "11111"),
    User("kosyakkk", "525252")
]
def find_user(login: str, password: str):
    for user in users:
        if user.login == login and user.password == password:
            return user
    return None
found_user = find_user("kosyakkk", "525252")
if found_user:
    print(f"Найден юзер: {found_user.login}")
else:
    print("Юзер не найден.")