# def spam():
#     eggs = 'spam local'
#     print(eggs) # prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs) # prints 'bacon local'
#     spam()
#     print(eggs) # prints 'bacon local'

# eggs = 'global'
# bacon()
# print(eggs) # prints 'global'

def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)