
def variable_parameters_positional(*x):
    for item in x:
        if isinstance(item, (list, tuple)):
            for element in item:
                print(element)
        else:
            print(item)
    #return(x)


#print(variable_parameters_positional([1,2,3,4,5],[6,7,8],(9,0)))
#variable_parameters_positional([1,2,3,4,5],[6,7,8],(9,0))

#variable_parameters_positional(one=1, two=2, three=3)


def variable_parameters_keyword(**x):
    #return(x)
    for item in x:
        print(item,':', x[item])
#print(variable_parameters_keyword(one=1,two=2,three=3,four=4))
#print(variable_parameters_keyword(1,2,3,4))
#variable_parameters_keyword(one=1,two=2,three=3,four=4)


def variable_parameters_positional_keyword(*x,**y):
    return(x,y)

print(variable_parameters_positional_keyword(5,6,7,8,one=1,two=2,three=3,four=4))

# def variable_parameters_keyword_positional(**x,*y):
#     return(x,y)

# print(variable_parameters_keyword_positional(one=1,two=2,three=3,four=4,5,6,7,8))