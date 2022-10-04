# Author: Alfonso Beltran
# Start Data: 7/20/22
# Topics: File reading, GUI, Automation

# This application is a basic Income tracker with a basic GUI.
# The purpose is to replicate what I do in a spread sheet and automate my monthly
# income tracking.

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


if __name__ == '__main__':

    fileName = 'income.csv'
    # Welcome user
    print("\nHello Slay\nWhat would you like to do\n")

    # Menu (Add new month, View precious months, Edit Prevous month)


    # View Months - Read File
    readFile(fileName)

    # Add month
    year = input("Enter Year: ")
    month = input("Enter Month: ")
    total_income = float(input("Enter Total Income: "))
    bills = float(input("Enter Bills: "))
    writeFile(fileName, year, month, total_income, bills)

    # Edit Month
    tempFile = NamedTemporaryFile(mode='w', delete=False)

    # https://stackoverflow.com/questions/46126082/how-to-update-rows-in-a-csv-file



    print('Slay')