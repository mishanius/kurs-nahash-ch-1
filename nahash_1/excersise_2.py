# TODO modify basic_if - if some_number greater then 5 it will return some_number else it will return 5
# in math this can be represented as max(5, some_number)
# example 1: basic_if(6) will return 6;
# example 2: basic_if(2) will return 5;
def basic_if(some_number):
    # write your code here remove the pass when finished
    if some_number>5:
        return some_number
    return 5

if __name__=="__main__":
    print(basic_if(3))