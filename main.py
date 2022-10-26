# Author: Alfonso Beltran
# Start Data: 7/20/22
# Topics: File reading, GUI, Automation

# This application is a basic Income tracker with a basic GUI.
# The purpose is to replicate what I do in a spread sheet and automate my monthly
# income tracking.

from calendar import month
from fileinput import filename
from tempfile import NamedTemporaryFile
import shutil
from posixpath import split
import csv
from csv import writer

def readFile(fileName):

    print("READING")
    dict_from_csv = {}

    dict_from_csv = csv.DictReader(open(fileName))
    for row in dict_from_csv:
        print(f'\t{row["Month"]}, {row["Year"]} income was {row["TotalIncome"]}')

def writeFile(fileName, year, month, total_income, bills):

    after_bills = round(total_income - bills, 2)
    savings = round(after_bills / 2, 2)
    monthly_spend = round(savings / 5 * 4, 2)
    weekly_spend = round(savings / 5, 2)

    print(after_bills)
    print(savings)
    print(monthly_spend)
    print(weekly_spend)

    print("WRITING")
    with open(fileName, 'a+', newline='') as csv_file:
        csv_writer = writer(csv_file)

        csv_writer.writerow([year, month, total_income, bills, after_bills, savings, monthly_spend, weekly_spend, weekly_spend])

def addMonth():
    year = input("Enter Year: ")
    month = input("Enter Month: ")
    total_income = float(input("Enter Total Income: "))
    bills = float(input("Enter Bills: "))
    writeFile(fileName, year, month, total_income, bills)

# TODO: Finish edit row feature.
def editMonth(fileName):



    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['ID', 'Name', 'Course', 'Year']
    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['ID'] == str(stud_ID):
                print('updating row', row['ID'])
                row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
            row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


if __name__ == '__main__':

    fileName = 'income.csv'
    # Welcome user
    print("\nHello Slay\nWhat would you like to do\n")

    # Menu (Add new month, View precious months, Edit Prevous month)
    while(True):
        print                  ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        menu_choice = int(input(" [1]< View Previous Months >, [2]< Add New Month >, [3]< Edit Previous Mont >, [4]< Exit > \n"))

        if menu_choice is 1:
            # View Months - Read File
            readFile(fileName)
        elif menu_choice is 2:
            # Add month
            addMonth()
        elif menu_choice is 3:
            # Edit Month
            print("Working on it! ( ͡ᵔ ͜ʖ ͡ᵔ) ")


        elif menu_choice is 4:
            break
        else:
            print("Unknown Option")


    print('Slay')