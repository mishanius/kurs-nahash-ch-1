from utils.register_utils import varify_name, get_current_year


# relevant video tutorial - https://sfsfd.sdsadf.asfdsfd

# TODO - write a function that tells if an age given to a person of certain age group is valid
# available age groups are - "child" (0-13], "teen" (13-18], grownup (18-67), senior [67-120)
# Example 1 calculate_age_group(14) will return "teen"
# Example 2 calculate_age_group(13) will return "child"
# Example 3 calculate_age_group(67) will return "senior"
def calculate_age_group(age):
    """
    :param age: an integer between o and 120 (including 120) a.k.a (0,120]
    :return: string representing the age group of this age, available age groups are -
            "child" (0-13],
            "teen" (13-18],
            "grownup" (18-67),
            "senior" [67-120)
    """
    pass


# TODO - write a function that given a birth year and a current year calculates the current age
def calculate_age(year_of_birth, current_year):
    """
    if wrong input return -1
    current year only can be greater than 2021
    year_of_birth only valid if greater then 1900
    :param current_year: an int
    :param year_of_birth: an int
    :return: the age as a whole number (integer)
    """
    pass


# TODO - write a function that gets name from user
def get_name():
    """
    if name is valid we will print "nice to meet you <the name client entered>"
    if name is not valid print to client name not valid
    :return: the name if it is valid or None if name not valid
    """
    pass


# TODO - write a function that gets y.o.b from user
def get_year_of_birth():
    """
    gets year of birth from client
    :return: the year of birth as integer
    """
    pass


def greet_user():
    """
    gets name from user if valid gets' year of birth
    prints to user "Hello dear <name> your age is <age> your group is <group>"
    """
    name = get_name()
    if name is None:
        print("you entered wrong name")
        return
    yob = get_year_of_birth("Enter your age")


# run this to play with you code
if __name__ == "__main__":
    name = input("give me name \n")
    print(f"is your name valid - {varify_name(name)}")
