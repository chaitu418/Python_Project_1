'''
    Decorators allow us to wrap another fucntion inorder to extedn the behaviour of wrapped function
    without permanently modifying it
'''
#1.Functions can be treated as objects
# def shout(text):
#     return text
#
# print(shout("hello"))
#
# cout=shout
# print(cout('Mellow'))

#2.Passing function as an argument

# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def greet(func):
#     greeting=func("Hi hello how are you")
#     print(greeting)
#
# greet(shout)
# greet(whisper)

#3.returning functions from another functions
