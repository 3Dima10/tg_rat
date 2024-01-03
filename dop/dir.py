import os


def list_directories(path=None):
    try:
        # Если путь не указан, используем домашнюю директорию пользователя
        if path is None:
            path = os.path.expandvars('%USERPROFILE%')
        
        # Получаем список файлов и директорий в указанном пути
        entries = os.listdir(path)
        
        # Выводим названия файлов и директорий на новых строках
        print("Список файлов и директорий в {}:".format(path))
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(f"[D] {entry}")  # [D] перед именем обозначает директорию
            else:
                print(f"[F] {entry}")  # [F] перед именем обозначает файл
        
        print("Derector {}\\".format(path))
        

    except Exception as e:
        print(f"Произошла ошибка: {e}")

while True:
    a = input("Ведите путь до деректорий :")
    if a == "esc..":
        break  

    elif a:
        list_directories(a)
    

    else:

        # Вызываем функцию без аргументов (по умолчанию - домашняя директория пользователя)
        list_directories()
    