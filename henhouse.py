"""
Cameron Macdonald
cim0061@arastudent.ac.nz

Car Sales Analysis Tool

A python program that will parse a CSV file into a list of dictionaries, each
containg data for one sale. A text menu will allow a user to select analytical functions
or output functions to a report text file.
"""


def load_sales(filename):
    """
    Opens CSV file and reads first line into a disposed header variable,
    then the rest of the data line by line into a list dictionaries.

    ARGS:    filename (str): CSV load path with file extension.
    RETURNS: sales_list (list of dictionaries): one dictionary per sale entry,
             keys are the header names, with sale_id/year as integers, price as float.
    """
    sales_list = []
    with open(filename) as fileread:
        header_line = fileread.readline()
        for line in fileread:
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
            sales_list.append(dict_build)
    return sales_list
final_list = load_sales("car_sales.csv")


def total_sales(sale_data):
    """
    Counts the number of sales entries.

    ARGS:    sale_data (list of dictionaries): sales entries to be counted.
    RETURNS: (int): number of sale entries in the list.         
    """
    return len(sale_data)


def total_revenue(sale_data):
    """
    Sums the price from sales entries.

    ARGS:    sale_data (list of dictionaries): sales entries to be summed.
    RETURNS: (float): Sum of all prices in sales entries.
         
    """
    total = 0.00
    for sale_price in sale_data:
        total = total + sale_price["price"]
    return total


def salesperson_count(count_data):
    """
    Counts the sales entries made by each salesperson and returns a dictionary of counts
    in format {name (str):count (int)}.

    ARGS:    count_data (list of dictionaries): sales entries to be counted.
    RETURNS: (dictionary): Salesperson names as keys paired to counts as values.
         
    """
    count_dict = {}
    for sale_dict in count_data:
        current_count = sale_dict["salesperson"]
        if current_count in count_dict:
            count_dict[current_count] = count_dict[current_count] + 1
        else:
            count_dict[current_count] = 1
    return count_dict


def most_sold_make(make_data):
    """
    Finds the most sold make by sales, returns it as a formatted string with a count.

    ARGS:    make_data (list of dictionaries) sales entries to be counted.
    RETURNS: (str): formatted string containing name and count of most sold make.
         
    """
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
    return (f"Make: {best_make}    Sales: {best_count}")


def least_sold_model(model_data):
    """
    Finds the least sold model by sales, returns it as a formatted string with a count.

    ARGS:    model_data (list of dictionaries): sales data to be counted.
    RETURNS: (str): formatted string containing name and count of least sold model.
         
    """
    model_counts = {}
    for sale_dict in model_data:
        current_keys = sale_dict["make"], sale_dict["model"]
        if current_keys in model_counts:
            model_counts[current_keys] = model_counts[current_keys] + 1
        else:
            model_counts[current_keys] = 1

    least_model = None
    least_count = float("inf")
    for current_keys in model_counts:
        current_count = model_counts[current_keys]
        if current_count < least_count:
            least_model = current_keys
            least_count = current_count

    make, model = least_model
    return (f"Make: {make}    Model: {model}    Sales: {least_count}")


def output_report(function_data):
    """
    Outputs all available analytical functions to an external text file.

    ARGS:    fucntion_data (list of dictionaries): sales data to be processed by fucntions.
    RETURNS: None
         
    """
    with open("Car_Sales_Report.txt", "w") as text_report:
        print(f"Total Sales - {total_sales(function_data)}\n", file=text_report)
        print(f"Total Revenue - ${total_revenue(function_data):,.2f}\n", file=text_report)
        print(f"Sales by Salesperson - {salesperson_count(function_data)}\n", file=text_report)
        print(f"Most Sold Make - {most_sold_make(function_data)}\n", file=text_report)
        print(f"Least Sold Model - {least_sold_model(function_data)}\n", file=text_report)
        

whitespace_buffer = "			"
menu_selection = (whitespace_buffer + "Welcome\n"
    "Please enter a number from the following options:\n"
                    "1) Total Sales\n"
                    "2) Total Revenue\n"
                    "3) Sales by Salesperson\n"
                    "4) Most Sold Make\n"
                    "5) Least Sold Model\n"
                    "6) Write All to Report File\n"
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
    
    elif user_input == "6" or user_input == "writereport":
        output_report(final_list)
        print(f"Report has been created.\n")

    elif user_input == "0" or user_input == "exit":
        break

    else:
        print("'" + user_input + "'" + " is not a valid option.\n")
