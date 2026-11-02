"""
Cameron Macdonald
cim0061@arastudent.ac.nz

Car Sales Analysis Tool

A python program that will parse a CSV file into a dictionary,
provide the user with analytic tools which will answer simple
questions from a text menu, and write those answers to a human readable
report file.
"""

"""
Goals
- load CSV
- parse each row into a dictionary
- answer some simple questions with analytics
- write answers to a short report file
"""

"""
Planning
- Map out main steps (parsing, analytical functions, text inteface, report out)
- Plan what steps needs what input, and what it is outputting
- Consider and implement testing methods
- Complete documentation
"""

final_list = []
def load_sales(filename):
    with open(filename) as fileread_var:
        header_line = fileread_var.readline()
        # split this up later so you can dynamically use the headers. Might be more trouble than it's worth
        for line in file_read_var:
            row_fields = line.strip().split(",")
            dict_build  = {
                "sale_id": int(row_fields[0]),
                "date": row_fields[1],
                "salesperson": row_fields[2],
                "make": row_fields[3],
                "model": row_fields[4],
                "year": int(row_fields[5]),
                "price": float(row_fields[6]),
                }
            final_list.append(dict_build)
    return final_list

menu_selection = ("Please select from one of the following options:\n"
                    "1) Total Sales\n"
                    "2) Revenue\n"
                    "3) Salesperson\n"
                    "4) Most Popular Make\n"
                    "5) Least Popular Make\n")
user_input = input(menu_selection)
if user_input.lower() == "1" or "total" or "sales" or "total sales":
    # function for total sales
    print("This is the placeholder for option 1")
elif user_input.lower() == "2" or "revenue":
    # function for revenue
    print("This is the placeholder for option 2")
elif user_input.lower() == "3" or "salesperson":
    # function for salesperson
    print("This is the placeholder for option 3")
elif user_input.lower() == "4" or "most popular make":
    # function for most popular make
    print("This is the placeholder for option 4")
elif user_input.lower() == "5" or "least popular make":
    # function for least popular make
    print("This is the placeholder for option 5")
else:
    print(user_input + " is not a valid option. " + menu_selection)
    # add a return to the beginning of the menu, or repeat the menu again?
    # maybe use a while loop to display the menu and then if/elif for option selection?