
# My first exercise 
'''
(BAD IDENTATION, DID YOU RUN THIS CODE BEFORE SUBMITTING?)
CORRECTION
drink_number = [1, 3, 7, 9, 11]
for drink in drink_number:
     print (drink)
 '''

drink_number = [1, 3, 7, 9, 11]
 for drink in drink_number:
     print (drink)

# My second exercise
'''
PLEASE RUN YOUR CODE BEFORE SUBMITTING, SAME PROBLEM AS EXERCISE 1
'''
 ages = {
     "umar" :10,
     "Amina" : 20,
     "oluwasaye" : 30,
     "umar" : 27,
 }
 for (key, value) in ages.items():
     print (key, value)


# My third exercise
'''
PLEASE RUN YOUR CODE BEFORE SUBMITTING, BAD INDENTATION.
THE CODE STRUCTURE IS GOOD BUT WONT RUN
'''
 name = "Mahmud"
 count = 0

 print(name)
 while name == "Mahmud" and count < 10:
     count += 1
     print(count)
 if count == 10:
         print("Aisha")


# My fourth Exercise
 cities = ['Berlin', 'São Paulo', 'Tokyo', 'New York']

 for city in cities:
     if " " in city:
         continue
     print(city)


# My fifth Exercise
 numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

 for row in numbers:
     for num in row:
         print(num)


# My Assignment 1
numbers_3d = [
    [
        [0, 1, 2], [3, 4, 5], [6, 7, 8]
        ],
         [
        [9, 10, 11], [12, 13, 14], [15, 16, 17]
        ],
         [
        [18, 19, 20], [21, 22, 23], [24, 25, 26]
        ]
        ]

# Loop through the 3D list
#print(matrix) should be outside the row codnition. Code is correct, good job
for matrix in numbers_3d:
    for row in matrix:
        print(matrix)
        print(row)
        for num in row:
            print(num)



#My second assignment( add calculator)
#CORRECT
total = 0

while True:
    user_input = input("Enter a number or type 'add' to finish: ")
    if user_input.lower() == 'add':
        print(f"The final total sum is: {total}")
        break

    try:

        num = float(user_input)
        total =total + num
        print(f"Current total: {total}")

    except ValueError:
        print("Invalid input, please enter a valid integer or 'add' to finish.")



# My third assignment
#correct
for i in range(5, 0, -1):
    print(i)
print("Go!")

# My fourth assignment
#correct
for up, down in zip(range(0, 5), range(4, -1, -1)):
    print(f"{up} {down}")



# The fifth assignment(it was the hardest.)
#CORRECT

word = input("Input a word to reverse: ")

# Reverse the word using slicing
r_word = word[::-1]

print(f"Output: {r_word}")



# My sisxth assignment (end=" ") It keeps the numbers on the same line
#CORRECT
count = 0  # Initialize counter

for i in range(100):  # I Use a large range to ensure I can find the first 7 multiples
    if i % 7 == 0:
        print(i, end=" ")  # Print the multiple of 7
        count += 1
    if count == 7:
        break



# My last assignment
#CORRECT

sentence = "The quick brown fox jumps over the lazy dog"

vowels = "aeiouAEIOU"

# Create an empty list to store vowels
vowel_list = []

for char in sentence:
    if char in vowels:
        vowel_list.append(char)  # Add vowel to the list

# Print the list of vowels
print(vowel_list)
