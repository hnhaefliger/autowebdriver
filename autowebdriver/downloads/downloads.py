import requests
import zipfile
import tarfile
import warnings
import os
import platform
import shutil

def findExecutables(path):
    '''
    Find the driver executable in tree.
    '''
    found = []
    separator = '/'
    
    if platform.system() == 'Windows':
        separator = '\\'

    if path[-1] == separator:
        path = path[:-1]
        
    for file in os.listdir(path):
        if os.path.isfile(path + separator + file):
            if 'driver' in file:
                found.append([path + separator + file, file])

        else:
            found += findExecutables(path + separator + file)

    return found

def downloadAndExtract(url, path):
    '''
    Download and extract the file from a given url.
    '''
    download_output = path + url.split('/')[-1]
    extract_output = path + 'driver_dir'
    
    response = requests.get(url, stream=True)
    iterable = response.iter_content(chunk_size=1024)

    with open(download_output, 'wb+') as f: # save zip file
        for chunk in iterable:
            f.write(chunk)

    if '.zip' in download_output:
        compressed_file = zipfile.ZipFile(download_output, 'r') # open zip file
        iterable = compressed_file.infolist() # get list of zipped contents

    elif '.tar' in download_output:
        if '.gz' in download_output:
            mode = 'r:gz'
          
        elif '.bz2' in download_output:
            mode = 'r:bz2'
            
        elif '.xz' in download_output:
            mode = 'r:xz'
            
        else:
            mode = 'r'
        
        compressed_file = tarfile.open(download_output, mode) # open tar file
        iterable = compressed_file.getmembers() # get list of tar contents

    else:
        raise Exception('Unsupported compression type')

    for file in iterable: # extract files
        compressed_file.extract(file, path=extract_output)

    os.remove(download_output)
    file = findExecutables(path + 'driver_dir')[0]
    shutil.move(file[0], path)
    shutil.rmtree(path + 'driver_dir')
    
    return path + file[1]
