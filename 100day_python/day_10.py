#Multiple Return Functions
def format_name(first_name:str, last_name:str):
    #Docstring
    """Format the first and last name to be capitalized."""
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    return f"{first_name.title()} {last_name.title()}"


print(format_name(input("Enter your first name: "), input("Enter your last name: ")))