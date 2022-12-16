# README

## Requirements
    Problem:

    XXX wants to generate insight from a list of banking transactions occurring in customer accounts. We want to generate minimum , maximum, and ending balances by month for customers. You can assume starting balance at beginning of the month is 0. You should read transaction data from csv files and produce output in the format mentioned below. 

    Please apply credit transactions first to calculate the balance on a given day.  Please write clear instructions on how to run your program on a local machine. Please use the dataset in Data Tab to test your program. You do not need to add a Column Header in the output. please assume the input file does not have a header row.

    Input CSV Format:
    CustomerID, Date, Amount

    Output Format:
    CustomerID, MM/YYYY, Min Balance, Max Balance, Ending Balance

## Before running the program:
    Please check if you have all the modules in the requirements.txt
    Quick check usage: pip install -r requirements.txt

## Running the program:
    Running the following command on the command line

    $ python3 accountTrans.py -f inputFileName.csv

    or

    $ python3 accountTrans.py --FileName inputFileName.csv

    The output data is in the output.csv
