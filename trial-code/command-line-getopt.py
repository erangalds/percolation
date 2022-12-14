## Passing Command line arguments and using getopt module to handle
import getopt
import sys
 
argv = sys.argv[1:]
 
opts, args = getopt.getopt(argv, 'x:y:')
 
# list of options tuple (opt, value)
print(f'Options Tuple is {opts}')
 
# list of remaining command-line arguments
print(f'Additional Command-line arguments list is {args}')

## To Execute run below
### python3 command-line-getopt.py -x 1 -y eranga A B