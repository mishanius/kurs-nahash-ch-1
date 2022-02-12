# This is a comment 123123

# hello_world is a function
# TODO modify the hello_world function so it would recive 2 paramets <name> and <family>
# example: hello("ploni", "almoni") will return "hello ploni almoni"
def hello_world(f_name, l_name):
    # this is variable assignment
    to_print = "hello " + f_name + ' ' + l_name
    # this is a return statemnt
    return to_print

# run this to play with you code
if __name__=="__main__":
    print(hello_world("ploni", "almoni"))
    #this ^^^ should be like this:
    # print(hello_world("ploni", "almoni"))