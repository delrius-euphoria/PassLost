import os, appdirs

appname = "PassLost"

def create():
    try:
        directory = appdirs.user_data_dir(appname)
        os.makedirs(directory)
    except FileExistsError:
        pass

def writer(directory):
    path = appdirs.user_data_dir(appname)
    try:
        with open(path+'/current_dir.dat','w') as file:
            file.write(directory)
    except FileNotFoundError:
        create()
        writer(directory)

def reader():
    try:
        path = appdirs.user_data_dir(appname)
        with open(path+'/current_dir.dat','r') as file:
            data = file.read()
        
        return data
    except FileNotFoundError:
        create()
        writer('')
        reader()
