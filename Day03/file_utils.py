with open("emails.txt", 'r') as email_file:
    read_file = email_file.read()

def valid_email(email):
    with open('valid_emails.txt', 'a') as valid_emails:
       valid_emails.write(email + "\n")

def invalid_email(email):
    with open('invalid_emails.txt', 'a') as invalid_emails:
        invalid_emails.write(email + "\n")

