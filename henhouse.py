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
- load CSV (DONE)
- parse each row into a dictionary (DONE)
- answer some simple questions with analytics (WIP)
- write answers to a short report file
- write documentation
"""

"""
Planning
- Map out main steps (parsing (DONE), analytical functions (DONE), text inteface (DONE), report out)
- Plan what steps needs what input, and what it is outputting (DONE)
- Consider and implement testing methods
"""

final_list = []
def load_sales(filename):
    """
Opens CSV file and reads first line into a header variable,
then the rest of the data line by line into a list dictionaries.

ARGS:

RETURNS: List of dictionaries
"""
    with open(filename) as fileread_var:
        header_line = fileread_var.readline()
        # split this up later so you can dynamically use the headers. Might be more trouble than it's worth
        for line in fileread_var:
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
load_sales("car_sales.csv")

def total_sales(sale_id):
    return len(sale_id)

def total_revenue(sale_data):
    total = 0.00
    for sale_price in sale_data:
        total = total + sale_price["price"]
    return total

def salesperson_count(count_data):
    count_dict = {}
    for sale_dict in count_data:
        current_count = sale_dict["salesperson"]
        if current_count in count_dict:
            count_dict[current_count] = count_dict[current_count] + 1
        else:
            count_dict[current_count] = 1
    return count_dict

def most_sold_make(make_data):
    make_counts = {}
    for sale_dict in make_data:
        current_make = sale_dict["make"]
        if current_make in make_counts:
            make_counts[current_make] = make_counts[current_make] + 1
        else:
            make_counts[current_make] = 1
    best_make = None
    best_count = 0
    for current_make in make_counts:
        current_count = make_counts[current_make]
        if current_count > best_count:
            best_count = current_count
            best_make = current_make
    return str(f"Make: {best_make}    Sales: {best_count}")

def least_sold_model(model_data):
    model_counts = {}
    for sale_dict in model_data:
        current_model = sale_dict["model"]
        if current_model in model_counts:
            model_counts[current_model] = model_counts[current_model] + 1
        else:
            model_counts[current_model] = 1
    least_model = None
    least_count = float("inf")
    for current_model in model_counts:
        current_count = model_counts[current_model]
        if current_count < least_count:
            least_count = current_count
            least_model = current_model
    return str(f"Model: {least_model}    Sales: {least_count}")

def output_report(final_list):
    with open("Car_Sales_Report.txt", "w") as text_report:
        print(f"Total Sales: {total_sales(final_list)}", file=text_report)
        print(f"Total Revenue: {total_revenue(final_list)}", file=text_report)
        print(f"Sales by Salesperson: {salesperson_count(final_list)}", file=text_report)
        print(f"Most Sold Make: {most_sold_make(final_list)}", file=text_report)
        print(f"Least Sold Model: {least_sold_model(final_list)}", file=text_report)
        

whitespace_buffer = "			"
menu_selection = (whitespace_buffer + "Welcome\n"
    "Please enter a number from the following options:\n"
                    "1) Total Sales\n"
                    "2) Total Revenue\n"
                    "3) Sales by Salesperson\n"
                    "4) Most Sold Make\n"
                    "5) Least Sold Model\n"
                    "6) Average Sale by Salesperson\n"
                    "7) Top Salesperson by Average Sale\n"
                    "8) Sales by Month\n"
                    "9) Best Month by Revenue\n"
                    "10) Write All to Report File\n"
                    "0) Exit\n"
                    ">"
                  )

while True:
    user_input = input(menu_selection).lower().strip()
    
    if user_input == "1" or user_input == "totalsales":
        print(f"Total Sales: {total_sales(final_list)}\n")

    elif user_input == "2" or user_input == "totalrevenue":
        print(f"Total Revenue: ${total_revenue(final_list):,.2f}\n")
    
    elif user_input == "3" or user_input == "salesbyperson":
        print(f"{salesperson_count(final_list)}\n")

    elif user_input == "4" or user_input == "mostsold":
        print(f"{most_sold_make(final_list)}\n")

    elif user_input == "5" or user_input == "leastsold":
        print(f"{least_sold_model(final_list)}\n")
    
    elif user_input == "10" or user_input == "writereport":
        print(f"{output_report(final_list)}\n")

    elif user_input == "0" or user_input == "exit":
        break

    else:
        print("'" + user_input + "'" + " is not a valid option.\n")

