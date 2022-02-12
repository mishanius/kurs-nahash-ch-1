# This is a comment 123123

# hello_world is a function
# TODO modify the hello_world so it would recive 2 paramets <name> and <family>
# example: hello("ploni", "almoni") will return "hello ploni almoni"
def hello_world(name, family):
    # this is variable assignment
    to_print = "hello " + name + " " + family
    # this is a return statemnt
    return to_print

if __name__=="__main__":
    print(hello_world("ploni", "almoni"))