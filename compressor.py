import os
import patoolib
import zipfile

from time import time

available_methods = ['zip', 'rar', 'targz'] # Métodos disponíveis

class Compressor:
    # Constrututor com método e arquivo alvo
    def __init__(self, method: str, file):
        if not any(extension in method for extension in available_methods):
            raise Exception('Invalid method')
        
        self.method = method
        self.file = file
    
    # Comprimi arquivo baseado no método
    def compress_file(self):
        if self.method == 'zip':
            result, exec_time = self.zip_compressor()
        elif self.method == 'rar':
            result, exec_time = self.rar_compressor()
        else:
            result, exec_time = self.targz_compressor()

        return result, exec_time # Retornar tamanho do arquivo resultante e tempo de execução

    # Compressor zip
    def zip_compressor(self):
        start = time() # Horário de execução

        # Instância zip com 'w' de write e método de compressão DEFLATED
        my_zip = zipfile.ZipFile('assets/zip_compression.zip', 'w', compression=zipfile.ZIP_DEFLATED)
        
        if type(self.file) is str: # Caso seja arquivo, comprima
            my_zip.write(self.file) # Comprimi o arquivo escrevendo no arquivo resultante
        else: # Caso seja pasta, itere
            for file in self.file:
                my_zip.write(file)

        my_zip.close() # Fecha instância

        end = time() # Horário do término

        return self.get_file_size('assets/zip_compression.zip'), end - start # Tamanho do arquivo e tempo de execução

    # Compressor rar
    def rar_compressor(self):
        start = time() 
        
        if type(self.file) is str:
            file = (self.file,)
        else:
            for file in self.file:
                file = tuple(self.file) # Transforma lista em tuple
        
        # Cria arquivo resultante selecionando o método baseado na string, ou seja, identifica o método pela extensão
        # Patoolib executa ferramenta externa baseado no nome do aqruivo (exemplo: Se o nome do arquivo possuir '.rar' ele executa o comando rar no terminal)
        patoolib.create_archive('assets/rar_compression.rar', file, verbosity=-1)

        end = time()

        return self.get_file_size('assets/rar_compression.rar'), end - start
    
    # Compressor tar.gz
    def targz_compressor(self):
        start = time() 
        
        if type(self.file) is str:
            file = (self.file,)
        else:
            for file in self.file:
                file = tuple(self.file)
        
        patoolib.create_archive('assets/targz_compression.tar.gz', file, verbosity=-1)

        end = time()

        return self.get_file_size('assets/targz_compression.tar.gz'), end - start

    
    # Retorna tamanho do arquivo
    def get_file_size(self, file_name: str):
        file_stats = os.stat(file_name)
        return file_stats.st_size

    