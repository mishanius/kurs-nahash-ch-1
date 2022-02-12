# TODO In this excercise we are going to iterate over a list and sum all of its numbers
# example 1: basic_loop([1,2]) will return 3
# example 2: basic_loop([1]) will return 1
def basic_loop(list_of_numbers):
    total_sum=0
    for number in list_of_numbers:
        total_sum += number
    return total_sum

if __name__=="__main__":
    print(basic_loop([1,2,3]))