import os
import hashlib

BLOCK_SIZE = 65536

def get_file_list(dirName):
    try:
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles = allFiles + get_file_list(fullPath)
            else:
                allFiles.append(fullPath)
        return allFiles
    except FileNotFoundError as ex:
        raise FileNotFoundError('No such Directory: {dir}. Please check directory name'.format(dir=dirName))

def hash_generator(fileList):
    fileListWithHash = []
    for file in fileList:
        fileHash = hashlib.sha512()
        print(file)
        with open(file, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0 :
                fileHash.update(fb)
                fb = f.read(BLOCK_SIZE)
        fileListWithHash.append((file, fileHash.hexdigest()))
    print (fileListWithHash)
    return fileListWithHash

def detectDupes(fileListWithHash):
    dupes_removed_dict = {fileAndHash[1]: fileAndHash[0] for fileAndHash in fileListWithHash}
    # can simply return dupes_removed_dict.values() if you need a list of files that simply needs to be retained
    dupes = [fileAndHash for fileAndHash in fileListWithHash if fileAndHash[0] not in dupes_removed_dict.values()]
    return dupes

def sorter_deleter(dirName):
    fileList = get_file_list(dirName)
    hashedFileList = hash_generator(fileList)
    duplicateFiles = detectDupes(hashedFileList)
    print('done')


if __name__=='__main__':
    dirName='./test'
    sorter_deleter(dirName)