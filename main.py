import os
from compressor import Compressor, available_methods

def clear_dir():
  files = os.listdir('assets')
    
  for file in files:
    os.remove('assets/%s' % file)


def main():
  files = os.listdir('sample')

  files.sort()

  # single file
  for file in files:
    clear_dir()

    sample_size = round(os.stat('sample/%s' % file).st_size / 1000, 3)

    print(f'\n{file} = {sample_size} Kb\n')

    for method in available_methods:
      compressor = Compressor(method, 'sample/%s' % file)
      size, exec_time = compressor.compress_file()

      size = round(size / 1000, 3)
      exec_time = round(exec_time * 1000, 3)

      print(f'{method}: {size} Kb, {exec_time} ms, {round((sample_size - size) / exec_time, 3)} Kb/ms')
  
  # multiple files
  clear_dir()

  files_paths = [] 
  dir_sample_size = 0
  
  for i in range(len(files)):
    files_paths.append('sample/%s' % files[i])
    dir_sample_size = dir_sample_size + os.stat('sample/%s' % files[i]).st_size

  dir_sample_size = round(dir_sample_size / 1000, 3)

  print(f'\ndirectory size = {dir_sample_size} Kb\n')
  
  for method in available_methods:
    compressor = Compressor(method, files_paths)
    size, exec_time = compressor.compress_file()

    size = round(size / 1000, 3)
    exec_time = round(exec_time * 1000, 3)

    print(f'{method}: {size} Kb, {exec_time} ms, {round((dir_sample_size - size) / exec_time, 3)} Kb/ms')

if __name__ == '__main__':
  main()