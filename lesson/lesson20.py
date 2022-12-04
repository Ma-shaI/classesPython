# Модуль OS и OS.PATH

import os

# print('Текущая директория: ', os.getcwd())  # C:\Users\Компьютер\OneDrive\Рабочий стол\Project\lesson
#
# print(os.listdir())  # возвращает список директорий и файлов, находящихся в текущей директории
#
# print(os.listdir(".."))

# os.mkdir("folder")  # создает директорий по указанному пути
# os.makedirs('nested1/nested2/nested4')  # создает промежуточные директории и конечную, указанные в пути, если они
# не существуют. Если конечная директория уже существует, то будет сгенерированна ошибка FileExistsError

# os.remove('xyz.txt')  # удаление файла

# os.rename('nested1', 'test')  # переименовывает файл или директорию
# os.rename('test.txt', 'test/test1.txt')  # переименовывает файл или директорию, перемещает файлы в существующие
# директории

# os.renames('text2.txt', 'test1/test1.txt') # переименовывает файл или директорию, создавая директории и переместил
# файл

# os.rmdir('test1') # удаляет пустую директорию

# for root, dirs, files in os.walk('test', topdown=True):  # Возвращает имена объектов в виде дерева директорий. Для
#     # каждой директории возвращает кортеж(root - путь к директории, dirs-список директорий, files-список файлов
#     print('Root:', root)
#     print('  Subdirs:', dirs)
#     print('  Files:', files)

#
# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#
#
# remove_empty_dirs('test')

# print(os.path.split(r'C:\Users\Компьютер\OneDrive\Рабочий стол\Project\lesson\test\nested3\test1.txt'))
# разбивает путь на кортеж (head, tail), tail - последний компонент пути, head - все остальное

# print(os.path.dirname(r'C:\Users\Компьютер\OneDrive\Рабочий стол\Project\lesson\test\nested3\test1.txt'))
# возвращает имя директории
# print(os.path.basename(r'C:\Users\Компьютер\OneDrive\Рабочий стол\Project\lesson\test\nested3\test1.txt'))
# возвращает имя файла

# print(os.path.join(r'C:\Users\Компьютер\OneDrive\Рабочий стол\Project\lesson', 'files', 'dir', 'three.txt'))


# dirs = ['Work/F1', 'Work/F2/F21']
#
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()
#
# file_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
#
# for file in file_text:
#     with open(file, 'w') as f:
#         f.write(f'Текст для файла по пути {file}.')


print("Обход Work снизу вверх")
for root, dirs, files in os.walk('Work', topdown=False):

    print(root)
    print(dirs)
    print(files)

print()
print("Обход Work сверху вниз")
for root, dirs, files in os.walk('Work', topdown=True):

    print(root)
    print(dirs)
    print(files)