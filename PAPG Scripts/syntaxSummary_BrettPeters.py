age = 33    # A number data type - Specifically an int

name = 'Brett'  # A string data type. 'Brett' is the string literal and Brett is the actual string.

states = ['Texas', 'Missouri', 'New York', 'New Hampshire']     # A List data type

carFeatures = ('red', 2007, 65835193046, 'Toyota', 3.0)     # A Tuple data type (immutable)

addresses = {'Smith': 4540, 'Williams': 4400, 'Simpson': 4743}   # A Dictionary data type

print(age, type(age))
print(name, type(name))
print(states, type(states))
print(carFeatures, type(carFeatures))
print(addresses, type(addresses))

'''
STATIC VS. DYNAMIC TYPE PROGRAMMING

Static type is checking types during the compiling process and dynamic type 
is checked at run time of the program.

Both data types determine what functions objects can do, but static typing stores an object 
where only allowed operations will be able to be performed, while dynamic type stores the 
type with the object and then checks the operations performed against the objects capabilities.

'''
