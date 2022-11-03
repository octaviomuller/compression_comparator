import os
import patoolib
import zipfile

from time import time

available_methods = ['zip', 'rar', 'targz']

class Compressor:
    def __init__(self, method: str, file):
        if not any(extension in method for extension in available_methods):
            raise Exception('Invalid method')
        
        self.method = method
        self.file = file
    
    def compress_file(self):
        if self.method == 'zip':
            result, exec_time = self.zip_compressor()
        elif self.method == 'rar':
            result, exec_time = self.rar_compressor()
        else:
            result, exec_time = self.targz_compressor()

        return result, exec_time

    def zip_compressor(self):
        start = time()

        my_zip = zipfile.ZipFile('assets/zip_compression.zip', 'w', compression=zipfile.ZIP_DEFLATED)
        
        if type(self.file) is str:
            my_zip.write(self.file)
        else:
            for file in self.file:
                my_zip.write(file)

        my_zip.close()

        end = time()

        return self.get_file_size('assets/zip_compression.zip'), end - start

    def rar_compressor(self):
        start = time() 
        
        if type(self.file) is str:
            file = (self.file,)
        else:
            for file in self.file:
                file = tuple(self.file)
        
        patoolib.create_archive('assets/rar_compression.rar', file, verbosity=-1)

        end = time()

        return self.get_file_size('assets/rar_compression.rar'), end - start
    
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

    def get_file_size(self, file_name: str):
        file_stats = os.stat(file_name)
        return file_stats.st_size

    