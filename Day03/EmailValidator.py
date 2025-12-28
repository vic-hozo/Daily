from validator import pattern
from file_utils import read_file, valid_email, invalid_email
import re

emails = read_file.splitlines() #assigning emails.txt contents with re.compile()

for email in emails:
    if re.match(pattern, email):
     valid_email(email)
    else:
     invalid_email(email)









    






