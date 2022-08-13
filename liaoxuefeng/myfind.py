import os

def myfind(filestring,filepath='.'):
    for i in  os.listdir(filepath):
        i_fullpath = os.path.join(filepath,i)
        if os.path.isfile(i_fullpath) and filestring in i:
            print(i_fullpath)
        elif os.path.isdir(i_fullpath):
            #print(os.path.join(filepath,i))
            return myfind(filestring,i_fullpath)

myfind('py')            