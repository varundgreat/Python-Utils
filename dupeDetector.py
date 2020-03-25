import os
import hashlib

BLOCK_SIZE = 65536

def get_file_list_with_size(dirName):
    if os.path.exists(dirName):
        counter =0
        filepaths = []
        filenames = get_file_list(dirName)
        # for basename in os.listdir(dirName):
        #     print (basename)
        #     #print ('\n')
        #     #print os.path.isfile()
        #     print (os.path.join(dirName, basename))
        #     print (os.path.isfile(os.path.join(dirName, basename)))
        #     counter+=1
        #     print (counter)
        for i in range(len(filenames)):
            print(filenames[i])
            file_path=os.path.join(dirName, filenames[i])
            filepaths.append((file_path, os.path.getsize(file_path)))
            print(filepaths[i])
        print (len(filenames))
        return filepaths
    return


def get_file_list(dirName):
    filenames = []
    for basename in os.listdir(dirName):
        print (basename)
        if os.path.isfile(os.path.join(dirName,basename)):
            filenames.append(basename)
        else:
            print("not a file")
        print (len(filenames))
    return filenames


def hash_generator(fileList):
    fileListWithHash = []
    fileHash = hashlib.sha512()
    for file in fileList:
        print(file[0])
        with open(file[0], 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0 :
                fileHash.update(fb)
                fb = f.read(BLOCK_SIZE)
            print (fileHash.hexdigest())
        fileListWithHash.append((file[0], file[1], fileHash.hexdigest()))
    print (fileListWithHash)
    return fileListWithHash

def detectDupes(fileListWithHash):
    dupes = []
    for i in range(len(fileListWithHash)):
        j=i+1
        if (j<=len(fileListWithHash)):
            while fileListWithHash[i][2] == fileListWithHash[j][2] :
                dupes.append(fileListWithHash[i])
                j += 1
        else:
            break
        i = j
    return dupes

def sorter_deleter(dirName):
    if os.path.exists(dirName):
        fileList = get_file_list_with_size(dirName)
        fileList.sort(reverse=True, key= lambda x: x[1])
        hashedFileList = hash_generator(fileList)
        duplicateFiles = detectDupes(hashedFileList)
        print('done')




if __name__=='__main__':
    dirName='./test'
    sorter_deleter(dirName)