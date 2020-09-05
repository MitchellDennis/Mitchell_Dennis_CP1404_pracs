
"""emails"""

"""
need to:
get emails
seperation function
make dictionary
ask name function
"""


"""CONSTANTS"""

"""Main----------------------------------"""

def main():
    emails = get_emails()
    display_emails(emails)

"""Other functions------------------------"""
def get_emails():
    emails = {}
    user_email = "a"
    while user_email != "":
        user_email = input("Email: ")
        if user_email != "":
            emails[user_email] = get_name(user_email)

    return emails

def get_name(user_email):
    name_section = user_email.split('@')[0]
    multiple_names = name_section.split('.')
    name = " ".join(multiple_names).title()

    name_yn = input("Is your name {}? (Y/n)".format(name)).lower()
    if name_yn == "" or name =="y" or name == "yes":
        return name
    else:
        name = input("Name: ")
        return name

def display_emails(emails):
    for email in emails:
        print("{} ({})".format(emails[email], email))

"""run------------------------------------"""
main()