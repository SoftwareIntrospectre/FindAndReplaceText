import os

def write_to_file():
        
        with open("C:\\Users\\Tony Chacon\\PythonPracticeApps\\FindAndReplace\\FindAndReplace_Document.txt", "r+") as f:
                write_contents = f.write("")
                read_contents = f.readline()

                write_contents
                read_contents
                print(read_contents)

write_to_file()
