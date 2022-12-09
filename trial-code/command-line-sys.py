## Example of passing command line arguments for processing
import sys
 
if len(sys.argv) != 3:
    raise ValueError('Please provide email-id to send the email.')
 
print(f'Script Name is {sys.argv[0]}')
 
email = sys.argv[1]

name = sys.argv[2]

print(f'Sending test email to {email}')
print(f'Name is {name}')

## To execute run below
## python3 command-line-sys.py erangalds@gmail.com 