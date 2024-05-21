"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
flag = True
question_age = None
while flag:
    temp_age = input("Enter your age, please: ")
    if not (temp_age.isdigit()):
        print("Input is incorrect")
    else:
        question_age = int(temp_age)
        flag = False


def main(age: int) -> str:
    profession = None
    if 0 < age < 7:
        profession = "Attends kindergarten"
    elif 7 <= age < 18:
        profession = "Attends school"
    elif 18 <= age < 23:
        profession = "Attends institute"
    else:
        profession = "Attends dream job"
        return profession


if __name__ == "__main__":
    activity = main(question_age)
    print(f"Type of activity: {activity}")
