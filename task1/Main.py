from os.path import exists
from CSV_creat import creating
from File_writ import writing_scv
from File_writ import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()