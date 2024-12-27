''''
The keyword def introduces a function definition. 
It must be followed by the function name and the parenthesized list of formal parameters. 
The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; 
this string literal is the function’s documentation string, or docstring. 
There are tools which use docstrings to automatically produce online or printed documentation, 
or to let the user interactively browse through code; 
it’s good practice to include docstrings in code that you write, so make a habit of it.

The execution of a function introduces a new symbol table used for the local variables of the function. 
More precisely, all variable assignments in a function store the value in the local symbol table; 
whereas variable references first look in the local symbol table, 
then in the local symbol tables of enclosing functions, 
then in the global symbol table, and 
finally in the table of built-in names. 
Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function 
(unless, for global variables, named in a global statement, 
or, for variables of enclosing functions, named in a nonlocal statement),
 although they may be referenced.


 The actual parameters (arguments) to a function call are introduced in the local symbol table of the 
 called function when it is called; 
 thus, arguments are passed using call by value (where the value is always an object reference, 
 not the value of the object). 
 [1] When a function calls another function, or calls itself recursively, 
 a new local symbol table is created for that call.

A function definition associates the function name with the function object in the current symbol table. 
The interpreter recognizes the object pointed to by that name as a user-defined function. 
Other names can also point to that same function object and can also be used to access the function:


'''
'''
import symtable

st= symtable.symtable('''
global_var = 10

def func():
    global global_var
    global_var = 20
    return global_var

print(func())
print(global_var)
''', 'test','exec')
print(st)
'''

#### Define once and use as many as wanted
'''
def hello():
    print("Hello World")

hello()
hello()
hello()
hello()
'''
'''
def hello():
    return("Hello World")


h = hello()
print(h)
print(h)

'''
'''
def hello(default ="World"):
    print("Hello ",default)

hello()
hello("Samuael")
hello("Aster")
hello("Mikias")
hello("There")

'''

### Defining functions
'''
It is also possible to define functions with a variable number of arguments. 
There are three forms, which can be combined.
'''
### 1. Default Argument Values
'''
The most useful form is to specify a default value for one or more arguments. 
This creates a function that can be called with fewer arguments than it is defined to allow
The default values are evaluated at the point of function definition in the defining scope 

'''
'''
def greeting(name):
    print("Hello,", name)

greeting("Samuael") #positional
greeting(name="Aster") #keyword
'''

'''

def greeting(name):
    print("Hello,", name)


greeting()
'''
'''
def greeting(name):
    print("Hello,", name)


greeting(["Ayel","Lemma","Kebede"])

'''
'''
def say_hobbies(*hobbies):
    print("My hobbies")
    for hobby in hobbies:
        print("- ",hobby)

say_hobbies("Reading books", "Watching TV", "Playing football", "Travelling")

'''

'''
def say_hobbies(*hobbies):
    print("My hobbies")
    for hobby in hobbies:
        print("- ",hobby)

say_hobbies(One="Reading books", Two="Watching TV", Three="Playing football", Four="Travelling")
'''
'''
def say_hobbies(*hobbies):
    print("My hobbies")
    for hobby in hobbies:
        print("- ",hobby)

say_hobbies()

'''
'''
def say_hobbies(**hobbies):
    print("My hobbies")
    for hobby in hobbies:
        print(hobby,':',hobbies[hobby])

say_hobbies(One="Reading books", Two="Watching TV", Three="Playing football", Four="Travelling")

'''
'''
def say_hobbies(**hobbies):
    print("My hobbies")
    for hobby in hobbies:
        print(hobby,':',hobbies[hobby])

say_hobbies()
'''
'''
def say_hobbies(**hobbies):
    print("My hobbies")
    for hobby in hobbies:
        print(hobby,':',hobbies[hobby])

say_hobbies("Reading books", "Watching TV", "Playing football", "Travelling")
'''

'''
def greeting(name,/):
    print("Hello,", name)

greeting("Samuael") 
'''
'''
def detail(name,/, age):
    print("Name:", name)
    print("Age:", age)

detail("Samueal", age=25)
'''

'''
def detail(name, age, /, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail("Samueal", 25, phone="0950505050")
'''
'''
def detail(name, /, age, /, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail("Samueal", 25, phone="0950505050")
'''
'''

def detail(name, age, phone,/):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail(25, "0950505050","Samueal")
'''
'''
def detail(*,name, age, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail(name="Samueal", age=25, phone="0950505050")
'''
'''
def detail(*,name, age, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail("Samueal", age=25, phone="0950505050")
'''

'''
def detail(*,name, *,age, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail(name="Samueal", age=25, phone="0950505050")

'''
'''
def detail(*,name, age, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail("name"="Samueal", age=25, phone="0950505050")
'''
'''
def detail(*,name, age, phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail(Name="Samueal", Age=25, PHONE="0950505050")
'''
'''
def detail(name,/,age, *,phone):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail("Samueal", age=25, phone="0950505050")
'''
'''
def detail(*,name,age, phone,/):
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)

detail("Samueal", age=25, phone="0950505050")
'''

'''
def greeting(name, great="Good Morning"):
    print(great,',',name)

greeting("Samueal") # give only mandatory argument
'''
'''
def greeting(name, great="Good Morning"):
    print(great,',',name)

greeting("Samuael","Good afternoon") # give mandatory and optional arguments
'''
'''
name ="Aster"
def greeting(name, great="Good Morning"):
    print(great,',',name)

name ="Samuael"
greeting('Good Evening', name) 
'''
'''
def greeting(name, great="Good Morning"):
    print(great,',',name)
greeting() # TypeError: greeting() missing 1 required positional argument: 'name'
'''
'''
def greeting(name, great="Good Morning"):
    print(great,',',name)
greeting('Good Evening', name, 25) # TypeError: greeting() takes from 1 to 2 positional arguments but 3 were given
'''

'''
def greeting(great="Good Morning", name):
    print(great,',',name)
greeting(great='Good Evening',"Yohannes") #SyntaxError: parameter without a default follows parameter with a default
'''
'''
def greeting(name,great="Good Morning"):
    print(great,',',name)
greeting(great='Good Evening',"Yohannes")  # SyntaxError: positional argument follows keyword argument
'''
'''
### 2. keyword argument
def greeting(name, great="Good Morning"):
    print(great,',',name)
greeting(great='Good Evening', name="Yohannes")
greeting(name="Yohannes",great='Good Evening')
#greeting(name="Yohannes",great='Good Evening', gender="M") # TypeError: greeting() got an unexpected keyword argument 'gender'
#greeting(gender="M",great='Good Evening') # TypeError: greeting() got an unexpected keyword argument 'gender'
#greeting(great='Good Evening', "Ayantu") # SyntaxError: positional argument follows keyword argument
#greeting(name="Yohannes",great='Good Evening', great ="Good Afternoon") # SyntaxError: keyword argument repeated: great
#greeting("Abebe",name="Yohannes",great='Good Evening') # TypeError: greeting() got multiple values for argument 'name'

'''
'''
def county(name, *languages, **tourist_places):
    print('Country ',name)
    print("Around 80 langiages are speaking in ", name)
    for language in languages:
        print(language)
    print("-"*40)
    for place in tourist_places:
        print( tourist_places[place],' found in ' , place)

county("Ethiopia","Amharic","Oromifa","Trgigna","Somalic","Agew",hareri='Yejegol Ginb', Oromia="Sofomer Washa",Amhara="Lalibela")

'''

'''
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
response = ask_ok("Do you realy want to quit?")
print(response)
'''
### 3. Special parameters (simaple_calculator_2.py)
'''
By default, arguments may be passed to a Python function either by position or explicitly by keyword. 
For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer
need only look at the function definition to determine if items are 
passed by position, 
by position or keyword, or by keyword.
'''