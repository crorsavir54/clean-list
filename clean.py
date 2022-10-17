import csv
import re
import sys
import time
from more_itertools import unique_everseen
from pathlib import Path

file_name = Path(__file__).with_name('email-list.csv')
output_file_name = Path(__file__).with_name('mail-list_cleaned.csv')
# file_name = 'email-list.csv'
# output_file_name = 'email-list_cleaned.csv'

try:
    csv_reader = csv.reader(open(file_name, 'r'))
except FileNotFoundError:
    print("File not found! Please make sure the filename is [email-list.csv] and is in the same directory as this script.")
    sys.exit(1)

csv_writer = csv.writer(open(output_file_name, 'w'))

# Split name into first and last name
# This function assumes that the name is in the format of "First Last" 
# and the first word is the first name and remaining words are the last name
# Returns a tuple of the 0 first and 1 last name
def split_name(name):
    try:
        first_name, last_name = name.split(' ', 1) # Only split the first space
    except ValueError:
        first_name = name
        last_name = ''  
    return first_name, last_name

# Checks if it can find a valid email address on a given text
# If it can find an email, it will clean it with the parameters set
# It also peforms a special check to replace ".con" with ".com" at the end of the email
# However if .con is not in the end of the email, it will not be able to modify it
# Returns the cleaned emailif valid, else returns the input email as is
def clean_email(email):
    email = email.strip() #remove whitespaces from start and end of email
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', email)
    try:
        emails = str(emails[0]).lower()
        emails = re.sub('.con$', '.com', emails)
    except IndexError:
        email = email.strip()
        emails = "".join(email.split()).lower()
    
    return emails

def main():
    print("Cleaning email list...")
    header_row = ['Full Name', 'First Name', 'Last Name', 'Email']
    csv_writer.writerow(header_row)
    next(csv_reader) #skip header row
    
    for row in csv_reader:
        name = row[0]
        email = clean_email(row[1])
        first_name, last_name = split_name(name)
        csv_writer.writerow([name, first_name, last_name, email])
    print("...")
    time.sleep(0.5)
    print("...")
    print("...Done cleaning email list! Check the output file [mail-list_cleaned.csv] for the results.")
    # WRITE ONLY UNIQUE EMAILS IN ANOTHER FILE
    # with open('email-list_cleaned.csv', 'r') as f, open('unique-list.csv', 'w') as out_file:
    #     out_file.writelines(unique_everseen(f))

    # with open('email-list_cleaned.csv', 'r') as t1, open('unique-list.csv', 'r') as t2:
    #     fileone = t1.readlines()
    #     filetwo = t2.readlines()

    # with open('difference.csv', 'w') as outFile:
    #     for line in filetwo:
    #         if line not in fileone:
    #             outFile.write(line)

if __name__ == '__main__':
    main()