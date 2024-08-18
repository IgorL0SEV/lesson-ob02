# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).

# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют
# добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


class User:
    def __init__(self, us_id, us_name, us_access):
        self.__us_id = us_id  # number user
        self.__us_name = us_name  # name user
        self.__us_access = us_access  # access user

    def get_us_id(self):
        return self.__us_id

    def get_us_name(self):
        return self.__us_name

    def get_us_access(self):
        return self.__us_access

    def us_data(self):
        return {
            "id": self.get_us_id(),
            "name": self.get_us_name(),
            "access": self.get_us_access()
        }

    def set_us_id(self, us_id):
        self.__us_id = us_id

    def set_us_name(self, us_name):
        self.__us_name = us_name

    def set_us_access(self, us_access):
        self.__us_access = us_access

    def update_us_base(self, us_base, key):
        us_base[key] = self.us_data()


class Admin(User):
    def __init__(self, us_id, us_name, us_access, status_access):
        super().__init__(us_id, us_name, us_access)
        self.__status_access = status_access

    def get_status_access(self):
        return self.__status_access

    def set_status_access(self, status_access):
        self.__status_access = status_access

    def us_data(self):
        access_admin = super().us_data()
        access_admin["status_access"] = self.get_status_access()
        return access_admin


us_base = {}

user_1 = User(1, "Иванов", "user")
user_2 = User(2, "Петров", "user")
admin_1 = Admin(3, "Сидоров", "admin", "access")
admin_2 = Admin(4, "Сидоров", "admin", "not access")

us_base["user_1"] = user_1.us_data()
us_base["user_2"] = user_2.us_data()
us_base["admin_1"] = admin_1.us_data()
us_base["admin_2"] = admin_2.us_data()

for k, v in us_base.items():
    print(f"{k} = {v}")

print()
print (f"Удаление пользователя user_1")
print (f"Удаление администратора admin_2")
print()

if "user_1" in us_base:
    del us_base["user_1"]

if "admin_2" in us_base:
    del us_base["admin_2"]

for k, v in us_base.items():
    print(f"{k} = {v}")

print()
print (f"Добавление пользователя user_3")
print (f"Добавление администратора admin_3")
print()
user_3 = User(4, "Копейкин", "none")
admin_3 = Admin(6, "Лисичкина", "admin", "not access")
us_base["user_3"] = user_3.us_data()
us_base["admin_3"] = admin_3.us_data()

for k, v in us_base.items():
    print(f"{k} = {v}")

print()
print (f"Изменение статуса пользователя user_3: 'none' => 'user'")
print (f"Изменение статуса администратора admin_3: 'not access' => 'access'")
print()
user_3.set_us_access("user")
user_3.update_us_base(us_base,"user_3")
admin_3.set_status_access("access")
admin_3.update_us_base(us_base,"admin_3")

for k, v in us_base.items():
    print(f"{k} = {v}")
