import mymod
from mymodules import mymoddirectory

print(f'Name from module {mymod.name}')
print(f'Age from module {mymod.age}')

print('Calling a function in a module')
mymod.myself()

print(mymoddirectory.message)
