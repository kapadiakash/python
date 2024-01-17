# import os
# file_path = 'python.txt'

# print('---- Checking file exists using os.path.isexists()----')
# print(os.path.exists(file_path))

# if os.path.exists(file_path):
#     print(f'The file {file_path} does not exist.')
# else:
#     print(f'The file {file_path} does not exist.')
    
# print()


# #--------------------------------------------------------------------------------------


# import os

# file_path = 'python.txt'
# print('----checking file exists using os.path.isfile()----')
# print(os.path.isfile(file_path))

# if os.path.isfile(file_path):
#     print(f'The file {file_path} exists.')
# else:
#     print(f'The file {file_path} does not exist.')

# print()


print('--------------------------------------------------------------')

from pathlib import Path
file_path = Path('python.txt')

if file_path.is_file():
    print(f'The file {file_path} exists.')
else:
    print(f'The file {file_path} dies not exist.')