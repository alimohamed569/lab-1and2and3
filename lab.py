#program 8 lab 1
N = int(input("enter the number of apples "))
group_size = 7


groups_with_7 = N // group_size

apples_remaining = N % group_size

print(f"{groups_with_7} groups will contain exactly 7 apples, and {apples_remaining} apples will remain.")

#program 12 lab 1

units = int(input(" enter units: "))
tens = int(input("enter tens: "))
hundreds = int(input("enter hundreds: "))
if 0 <= units <= 9 and 0 <= tens <= 9 and 0 <= hundreds <= 9:
    result = hundreds * 100 + tens * 10 + units
    print("The number is:", result)
else:
    print("error")


#program 4 lab 2
N = int(input("Enter a number: "))
if N < 0:
    print("The number is negative.")
else:

    summation = 0

    for i in range(1, N + 1):
        summation += i

    print(summation)




#program 6 lab 2

N = int(input("Enter the number of elements: "))


sum_even = 0
sum_odd = 0


for i in range(N):
    num = int(input(f"Enter element {i + 1}: "))


    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print( sum_even)
print(sum_odd)


#program 9 lab 2

departure_time = input("Enter departure time (HH:MM): ")
arrival_time = input("Enter arrival time (HH:MM): ")
departure_parts = departure_time.split(':')
departure_hours = int(departure_parts[0])
departure_minutes = int(departure_parts[1])
arrival_parts=arrival_time.split(':')
arrival_hours=int(arrival_parts[0])
arrival_minutes=int(arrival_parts[1])
trip_hours = arrival_hours - departure_hours
trip_minutes = arrival_minutes - departure_minutes
if trip_minutes < 0:
    trip_hours -= 1
    trip_minutes += 60
print(f"Trip time: {trip_hours} hr and {trip_minutes} min")


#program 2 lab3

full_name = input("Enter name: ")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

print(first_name)
print(last_name)


#program 3 lab3

statement = input("Enter a statement: ")

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


vowel_count = 0


for char in statement:
    if char in vowels:
        vowel_count += 1

if vowel_count > 0:
    print(vowel_count)
else:
    print("No vowels found.")




#program 5 lab3

def is_valid_grade(grade):
    return 0 <= grade <= 100


grades = input("Enter a list of student grades separated by spaces: ").split()
grades = [int(grade) for grade in grades]

invalid_count = 0
validity_list = []
total_grade = 0
above_85_count = 0
above_avg_count = 0

for grade in grades:
    if is_valid_grade(grade):
        validity_list.append(1)
        total_grade += grade
        if grade > 85:
            above_85_count += 1
        if grade > total_grade / len(grades):
            above_avg_count += 1
    else:
        validity_list.append(0)
        invalid_count += 1

for valid in validity_list:
    if valid == 1:
        print("Valid")
    else:
        print("Invalid")

print("Number of invalid grades:", invalid_count)

print("Validity list:", validity_list)

if len(grades) > 0:
    average_grade = total_grade / len(grades)
    print("Average grade:", average_grade)

print("Students with grades greater than 85%:", above_85_count)

print("Students with grades greater than average:", above_avg_count)
