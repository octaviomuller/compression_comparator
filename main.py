import os
from compressor import Compressor, available_methods

# Limpa diretório
def clear_dir():
  files = os.listdir('assets')
    
  for file in files:
    os.remove('assets/%s' % file)


def main():
  files = os.listdir('sample') # Retorna os arquivos da pasta sample

  files.sort() # Ordena a lista de arquivos em ordem alfabética

  # Cenário de compressão de arquivo único (loop de aqruivos)
  for file in files:
    clear_dir() # Limpa diretório

    sample_size = round(os.stat('sample/%s' % file).st_size / 1000, 3) # Retorna tamanho do arquivo original

    print(f'\n{file} = {sample_size} Kb\n') # Imprimi tamanho do arquivo original

    # Iteração para cada método de compressão
    for method in available_methods:
      compressor = Compressor(method, 'sample/%s' % file) # Cria instância da classe compressora
      size, exec_time = compressor.compress_file() # Executa compressão do arquivo e retorna tamanho resultante e tempo de execução

      size = round(size / 1000, 3) # Transforma byte em kB e arredonda para 3 casas decimais
      exec_time = round(exec_time * 1000, 3) # Transforma segundos em ms e arredonda 3 casas

      print(f'{method}: {size} Kb, {exec_time} ms, {round((sample_size - size) / exec_time, 3)} Kb/ms') # Imprimi o método, tamanho resultante, tempo de execução e taxa de compressão
  
  # Cenário de compressão de pasta (compactação)
  clear_dir() # Limpa diretório

  files_paths = [] # Lista de caminhos
  dir_sample_size = 0 # Tamanho da pasta

  for i in range(len(files)):
    files_paths.append('sample/%s' % files[i])
    dir_sample_size = dir_sample_size + os.stat('sample/%s' % files[i]).st_size

  dir_sample_size = round(dir_sample_size / 1000, 3) # Transforma byte em kB e arredonda para 3 casas decimais

  print(f'\ndirectory size = {dir_sample_size} Kb\n') # Imprimi tamanho da pasta
  
  for method in available_methods:
    compressor = Compressor(method, files_paths)
    size, exec_time = compressor.compress_file()

    size = round(size / 1000, 3)
    exec_time = round(exec_time * 1000, 3)

    print(f'{method}: {size} Kb, {exec_time} ms, {round((dir_sample_size - size) / exec_time, 3)} Kb/ms')

if __name__ == '__main__':
  main()