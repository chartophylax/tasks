import random

HELP = """��������� �������:
help - ���������� �������
add - �������� ������
show  - ������� �� �����
random - ���������
exit - ����� �� ���������"""
RANDOM_TASKS = ["���������� �� ����", "�������� ����� ������", "��������� �����", "������ ������"] 
print (HELP)

def add_todo(date, task):
  if date in tasks: 
      tasks[date].append (task)
  else:
      tasks[date] = []
      tasks[date].append (task)
  print ("������", task, "��������� �� ����", date)


tasks = {}

while True:

  command = input("������� �������: ")

  if command == "help":
    print (HELP)
  elif command == "show":
    date = input ("������� ���� ��� ����������� ������ �����: ")
    if date in tasks:
      for task in tasks[date]:
        print ("-", task)
    else:
      print ("����� ���� ���")

  elif command == "exit":
    print("������� �� �������������! �� ��������!")
    break

  elif command == "add":
    date = input("������� ���� ��� ���������� ������: ")
    task = input("������� �������� ������: ")
    add_todo(date, task)

  elif command == "random":
    task = random.choice(RANDOM_TASKS)
    add_todo("�������", task)
  else:
    print ("����������� ��������")
