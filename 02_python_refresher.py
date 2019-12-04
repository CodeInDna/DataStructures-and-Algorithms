# Generators
# Below is an example of how to use a generator to print even numbers. 
# Printing all even numbers at once would take an infinite amount of 
# time, but the generator allows the process to pause, and go back to 
# creating even numbers when needed.

# Definition of the generator to produce even numbers.
def all_even():
	n=0
	while True:
		yield n
		n += 2
my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    # print(next(my_gen))	# 0 2 4 6 8
    pass


# We will create a generator fact_gen() that generates factorials. 
# For a number n, n factorial is denoted by n!, and it is the product 
# of all positive integers less than or equal to n. For example,
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def prod(a,b):
    return a * b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output

# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    # print(next(my_gen))	# 1 2 6 24 120
    pass


# write a function that checks sudoku squares for correctness.
def check_sudoku(square):
    # if len(square) != len(square[0]): 
    #     return False

    for row in square:
        check_list = list(range(1, len(square) + 1))
        for num in row:
            if num not in check_list:
                return False
            check_list.remove(num)

    for i in range(0, len(square)):
        check_list = list(range(1, len(square) + 1))
        for row in square:
            if row[i] not in check_list:
                return False
            check_list.remove(row[i])

    return True

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]
incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
print(check_sudoku(correct))    # True
print(check_sudoku(incorrect))  # False
print(check_sudoku(incorrect2)) # False
print(check_sudoku(incorrect3)) # False
print(check_sudoku(incorrect4)) # False
print(check_sudoku(incorrect5)) # False


# Python Class Practice
# Now let's assume that the current month is April, and you want to 
# use a Person class to help make use of information about the friends 
# in your contacts list. In particular, you'd like to increment the 
# age of all of your friends with birthdays in April. You would also 
# like to know who they are, along with their current ages, so you can 
# send them birthday cards. Finally, you would also like to figure out 
# which month has the most friends with birthdays, so you can budget 
# for all of the birthday cards you will need to buy.
class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month

    def birthday(self):
        self.age += 1

def create_person_objects(name, age, month):
    my_data = zip(name, age, month)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects

def get_april_birthdays(people):
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages 
    # as values. See the test below for an example expected output.
    april_birthdays = {}
    for person in people:
        if person.birthday_month.lower() == 'april':
            person.age += 1
            april_birthdays[person.name] = person.age
    return april_birthdays 

def get_most_comon_month(people):
    # Use the "month_count" dictionary to record counts of 
    # birthday months for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    month_count = {}
    for person in people:
        if person.birthday_month in month_count:
            month_count[person.birthday_month] += 1
        else:
            month_count[person.birthday_month] = 1
    max_count, month_name = 0, None
    for month in month_count.keys():
        if max_count < month_count[month]:
            max_count = month_count[month]
            month_name = month
    return month_name
     

# Here is the data for the test. Assume there is a single most common month.
names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna', 'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew', 'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John', 'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James', 'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur', 'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy', 'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James', 'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly', 'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald', 'David', 'Roger', 'Evan', 'Danny', 'William']
ages  = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85, 43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52, 66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88, 67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August', 'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April', 'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June', 'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March', 'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March', 'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September', 'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September', 'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August', 'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July', 'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
people = create_person_objects(names, ages, months)
print(get_april_birthdays(people))  # {'Michael': 11, 'Erica': 72, 'Carol': 36, ....}
print(get_most_comon_month(people)) # August
