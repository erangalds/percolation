## Handling Command line arguments using the argparse module
import argparse
 
# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument("language")
parser.add_argument("name")
 
# parse the arguments
args = parser.parse_args()
 
# get the arguments value
if args.language.title() == 'Python':
    print("I love Python too")
else:
    print("Learn Python, you will like it")
     
print(f'Hello {args.name}, this was a simple introduction to argparse module')

## To execute please run below
## python3 command-line-argparse.py python eranga