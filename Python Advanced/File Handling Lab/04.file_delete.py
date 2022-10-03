import os

try:
    os.remove('../03.file_writer/my_first_file.txt')
except FileNotFoundError:
    print('File already deleted')
