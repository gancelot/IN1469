from utils import copy_files, delete_common

dir1 = '../../task2_1_files/dir1'
dir2 = '../../task2_1_files/dir2'

results = copy_files(dir1, dir2)
print(f'{len(results)} files copied.')

results = delete_common(dir1, dir2)
print(f'{len(results)} files deleted.')
