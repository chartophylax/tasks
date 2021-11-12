import random

HELP = """Доступные команды:
help - напечатать справку
add - добавить задачу
show  - вывести на экран
random - случайная
exit - выход из программы"""
RANDOM_TASKS = ["Записаться на курс", "Написать Гвидо письмо", "Покормить Кошку", "Помыть машину"] 
print (HELP)

def add_todo(date, task):
  if date in tasks: 
      tasks[date].append (task)
  else:
      tasks[date] = []
      tasks[date].append (task)
  print ("Задача", task, "добавлена на дату", date)


tasks = {}

while True:

  command = input("Введите команду: ")

  if command == "help":
    print (HELP)
  elif command == "show":
    date = input ("Введите дату для отображения списка задач: ")
    if date in tasks:
      for task in tasks[date]:
        print ("-", task)
    else:
      print ("такой даты нет")

  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break

  elif command == "add":
    date = input("введите дату для добавления задачи: ")
    task = input("введите название задачи: ")
    add_todo(date, task)

  elif command == "random":
    task = random.choice(RANDOM_TASKS)
    add_todo("Сегодня", task)
  else:
    print ("неизвестная команада")
