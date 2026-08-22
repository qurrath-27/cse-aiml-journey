student = {
    "name": "qurrath",
    "age": 18,
    "college": "NSAKCET",
    "branch": "CSE(AIML)"
}
for key, value in student.items():
    print(key, ":", value)


student = {
    "name": "Ali",
    "math": 85,
    "python": 92,
    "DSA": 78
}
total = 0
count = 0
for key, value in student.items():
    if key != "name":
        total += value
        count += 1
print("Total:", total)
print("Average:", total / count)


students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 76,
    "Ayesha": 88,
    "Omar": 69
}
highest_student = ""
highest_mark = None
for key, value in students.items():
  if highest_mark is None or value > highest_mark:
          highest_student = key
          highest_mark = value

print("Highest student: ",key )
print("Highest mark: ",value)



product = {
    "name": "Notebook",
    "price": 50,
    "quantity": 4
}
total=None
for key, value in product.items():
    print(key, ":", value)
total = product["price"] * product["quantity"]
print("Total :" ,total)


def greet(name):
    print("Hello,", name)

greet("Qurrath")


def add(a, b):
    result = a + b
    return result

result = add(10, 20)
print(result)



def square(number):
    result =number*number
    return result
result = square(5)
print(result)


def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))



def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

result = factorial(5)
print(result)



def calculate_result(marks):
    total = 0
    highest = marks[0]
    lowest = marks[0]
    passed = 0
    failed = 0

    for number in marks:
        total += number

        if number > highest:
            highest = number

        if number < lowest:
            lowest = number

        if number >= 40:
            passed += 1
        else:
            failed += 1

    average = total / len(marks)

    return total, average, highest, lowest, passed, failed


marks = [85, 72, 91, 36, 68]

total, average, highest, lowest, passed, failed = calculate_result(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)