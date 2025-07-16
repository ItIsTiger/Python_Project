#Creating a dictionary in Python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    #"Loop": "The action of doing something over and over again.",
    "Data Type": "A classification of data which tells the compiler or interpreter how the programmer intends to use the data.",
    "List": "A collection of items in a particular order.",
    "Dictionary": "A collection of key-value pairs.",
    "Variable": "A reserved memory location to store values."
    }

# Accessing items in a dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary)

# Adding a new entry to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary = {}

#Wipe the dictionary
# programming_dictionary = {}

# Editing a dictionary
programming_dictionary["Bug"] = "A mistake in a program that causes it to behave unexpectedly."
print(programming_dictionary)

print("\n-----------------------------------------------------------------------------------------------------\n")

#Loop through a dictionary, you will get the key and need to access the value using the key
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")



student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

print("\n-----------------------------------------------------------------------------------------------------\n")

#Function to calculate student grades based on scores and return a new dictionary with grades
def cal_student_grades(scores: dict) -> dict:
    # Creating a new dictionary based on conditions from another dictionary
    student_grades = {}

    for key in scores:
        score = scores[key]
        if score >= 91:
            student_grades[key] = "Outstanding"
        elif 81 <= score < 91:
            student_grades[key] = "Exceeds Expectations"
        elif 71 <= score < 81:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"
    return student_grades

# Calling the function and printing the result
student_grades = cal_student_grades(student_scores)
# print(student_grades)

#Nesting dictionaries and lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

#Nesting dictionaries in dictionaries
travel_log_dict = {
    "France": {
        #Nesting a list in a dictionary
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log_dict["France"]["cities_visited"][0])  # Accessing nested data
print(travel_log[0]["cities_visited"][1])  # Accessing nested data in a list of dictionaries

#Nested Lists
Nested_List = ["A", "B", ["C", "D", "E"], "F"]
print(Nested_List[2][1])  # Accessing nested list element