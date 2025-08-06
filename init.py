import os

from termcolor import colored


class obtaining_the_necessary_information:
    def linux():
        directory_to_engine = input("Введите полный путь к движку(заканчивать на /) - ")
        if os.path.exists(directory_to_engine + "init.py"):
            print("Директория указана верно")
            
            with open("/temp/directory_to_engine" , "w") as fp:
                fp.write(directory_to_engine)
        
        else:
            print(colored("\n-----------------------------------------------------------------------------\nДиректория указана неверно , пожалуйста укажите правильную директорию\n-----------------------------------------------------------------------------\n" , "red"))
                
            work = True
            while work == True:        
                
                directory_to_engine = input("Введите полный путь к движку(заканчивать на /) - ")
                if os.path.exists(directory_to_engine + "init.py"):
                    print("Директория указана верно")
                    
                    with open("/temp/directory_to_engine" , "w") as fp:
                        fp.write(directory_to_engine)
                                
                    work = False
                    break
                    
                else:
                    print(colored("\n-----------------------------------------------------------------------------\nДиректория указана неверно , пожалуйста укажите правильную директорию\n-----------------------------------------------------------------------------\n" , "red"))
    
    def windows():
        directory_to_engine = input("Введите полный путь к движку(заканчивать на /) - ")
        if os.path.exists(directory_to_engine + "init.py"):
            print("Директория указана верно")
            
            with open("C:/windows/directory_to_engine" , "w") as fp:
                fp.write(directory_to_engine)
        
        else:
            print(colored("\n-----------------------------------------------------------------------------\nДиректория указана неверно , пожалуйста укажите правильную директорию\n-----------------------------------------------------------------------------\n" , "red"))
            
            work = True
            while work == True:
                
                directory_to_engine = input("Введите полный путь к движку(заканчивать на /) - ")
                if os.path.exist(directory_to_engine + "init.py"):
                    print("Директория указана верно")
                    
                    with open("C:/windows/directory_to_engine" , "w") as fp:
                        fp.write(directory_to_engine)
                        
                        work = False
                        break
                
                else:
                    print(colored("\n-----------------------------------------------------------------------------\nДиректория указана неверно , пожалуйста укажите правильную директорию\n-----------------------------------------------------------------------------\n" , "red"))
                    work = True
                    continue