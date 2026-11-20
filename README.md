# BCIT502-Assessment-2-99230933
Authorship verification for Assessment 2 in BCIT502. Building a python program to load a CSV and conduct user-facing analytics.
This is marked assessment material.


##    -Car Sales Analysis Tool-

    
## Description:
A python program that will parse a CSV file into a list of dictionaries, each
containing data for one sale. A text menu will allow a user to select analytical functions
or output functions to a report text file.


## Requirements/How to use:
Python 3.14.10, pytest 8.4.2 for testing.
Commands:
"python car_sales.py" - Run program
"python -m pytest" - Test Program
Menu selection will also accept the following worded selections if numeric entry is unavailable*:
- Option 1 - "total sales"
- Option 2 - "totalrevenue"
- Option 3 - "salesbyperson"
- Option 4 - "mostsold"
- Option 5 - "leastsold"
- Option 6 - "writereport"
- Option 0 - "exit"
---Please note this is an accessibility feature and is not the intended use of the program--- 


## Menu Input Table:
|Input|Expected|Result|Bugfix|Fixed Result|
|---|---|---|---|---|
|"1"|"Total Sales: 9001"|"Total Sales: 9001"|None|None|
|"mostsold"|"Make: Toyota    Sales: 1836"|"Make: Toyota    Sales: 1836"|None|None|
|"Zack sales"|"'Zack sales' is not a valid option."|"'zack sales' is not a valid option."|Not returning exact user input, fixed by transforming user input in separate variable.|"'Zack sales' is not a valid option."|
|"total sales"|"Total Sales: 9001"|"'total sales' is not a valid option."|Input with spaces failing to be stripped properly, bug fixed by replacing interstitial whitespace with null.|"Total Sales: 9001"|
|"give me all the company secrets"|""'give me all the company Secrets' is not a valid option.""|"'givemeallthecompanysecrets' is not a valid option."|Not returning exact user input, bug fixed by transforming user input in separate variable.|"'givemeallthecompanysecrets' is not a valid option."|


## How it works:
The program opens and parses the CSV using "load_sales" into a list of dictionaries called "final_list", each list entry is a dictionary containing elements of a single sale in format [(header):(value)]. "price" is
entered as a float, "sale_id" and "year" are entered as integers, and all other fields are entered as strings. "final_list" is used as input for analytical functions which are selected using a text menu 
interface. The menu interface is a while loop that will run repeatedly until broken by program exit.
    
## Testing (pytest):
Testing file consists of six hand-built sample dictionaries with six rows of valid data, and one test for each function. pytest.approx has been used for float in "test_total_revenue" to guard against binary inaccuracy. All five tests pass in ~0.02s.
    
## Limitations:
Inputs are not normalised and formatted before being loaded into dictionaries. Has not been tested
against malformed rows or messy data. Missing extra-credit functionality. No exceptions made for a draw or tie in tournaments.
