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
                "sale_id": int(row_fields[0])
                "date": row_fields[1]
                "salesperson": row_fields[2]
                "make": row_fields[3]
                "model": row_fields[4]
                "year": int(row_fields[5])
                "price": float(row_fields[6])
                }
            final_list.append(dict_build)
    return final_list
        