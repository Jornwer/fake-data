from mimesis import Person, Address
from sys import argv, stdout
from csv import *
import csv

def main():
    if len(argv) != 3:
        print("You must declare number of rows and region in ['en_US', 'ru_RU', 'uk_UA']: like 'python script.py 123 en_US'")
        return
    if not argv[1].isnumeric():
        print("You must declare number of rows: like 'python script.py 123 en_US'")
        return
    if argv[2] not in ['en_US', 'ru_RU', 'uk_UA']:
        print("You must declare region in ['en_US', 'ru_RU', 'uk_UA']: like 'python script.py 123 en_US'")
        return
    generatePeople(int(argv[1]), argv[2])

def generatePeople(row_num: int, region: str):
    if region == 'en_US':
        locale = 'en'
    elif region == 'ru_RU':
        locale = 'ru'
    else:
        locale = 'uk'
    writer = csv.writer(stdout, quoting=csv.QUOTE_NONE, delimiter=';', escapechar='"')
    person = Person(locale)
    address = Address(locale)
    for i in range(row_num):
        writer.writerow([person.full_name(), address.country(),
                        address.region(), address.city(), address.address(),
                        address.zip_code(),person.telephone()])

if __name__ == '__main__':
    main()