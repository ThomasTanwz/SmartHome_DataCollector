# This program cleans up the csv file
# filename: target file
# columns: how many columns does the file have?

import csv


def remove_foreign_characters(filename):
    with open(filename, 'r', newline='') as db, open(filename, 'a', newline='') as dbedit:
        mylist = db.readlines()
        for items in mylist:
            if (not items[0].isdigit()) and (not items[0] == '.'):
                print(items[0])
                newrole = items.replace(items[0], '')
                dbedit.write(newrole)


remove_foreign_characters("./DB.csv")
