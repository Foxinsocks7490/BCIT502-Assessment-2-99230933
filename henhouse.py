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


whitespace_buffer = "			"
menu_selection = (whitespace_buffer + "Welcome\n"
    "Please enter a number from the following options:\n"
                    "1) Total Sales\n"
                    "2) Total Revenue\n"
                    "3) Sales by Salesperson\n"
                    "4) Most Sold Make\n"
                    "5) Least Sold Make\n"
                    "6) Average Sale by Salesperson\n"
                    "7) Top Salesperson by Average Sale\n"
                    "8) Best Month by Revenue\n"
                  )
user_input = input(menu_selection).lower().strip()
if user_input == "1" or user_input == "totalsales":
    # function for total sales
    print("This is the placeholder for option 1")
elif user_input == "2" or user_input == "totalrevenue":
    # function for total revenue
    print("This is the placeholder for option 2")
elif user_input == "3" or user_input == "salesbyperson":
    # function for sales by salesperson
    print("This is the placeholder for option 3")
elif user_input == "4" or user_input == "mostsold":
    # function for most sold make
    print("This is the placeholder for option 4")
elif user_input == "5" or user_input == "leastsold":
    # function for least sold make
    print("This is the placeholder for option 5")
elif user_input == "6" or user_input == "averagesale":
    # function for average sale by salesperson
    print("This is the placeholder for option 6")
elif user_input == "7" or user_input == "topperson":
    # function for top salesperson by average sale
    print("This is the placeholder for option 7")
elif user_input == "8" or user_input == "bestmonth":
    # function for best month by revnue
    print("This is the placeholder for option 8")
else:
    print(user_input + " is not a valid option. ")
    # add a return to the beginning of the menu, or repeat the menu again?
    # maybe use a while loop to display the menu and then if/elif for option selection?
    # changed my mind, rewrite the whole thing. load valid inputs into a dictionary
    # as keys with a value of the function we want.