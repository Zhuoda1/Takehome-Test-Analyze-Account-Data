import csv
import getopt
import sys
import os

def inputProcess(fileName):
    """
    Process the input data to a list.

    :param fileName (string): the name of the csv file
    :return (list): the data list
    
    """ 
    
    data = []
    with open(fileName, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for inputrow in csvreader:
            # filter empty elements
            row = list(filter(None, inputrow))
            data.append(row)
    return data
    

def dataAnalyze(data):
    """
    Analyze data and output to a new file
    
    :param data (list) : the data list
    
    """
    if len(data) == 0:
        return
    
    # answer list    
    answerTab = []
    # current insight data
    curAnsRow = ['', '', 0, 0, 0]
    
    for row in data:
        
        if len(row) == 0:
            continue
        
        # get current id and month
        userID = row[0]
        date = row[1].split('/')
        month = date[0] + '/' + date[2]

        row[2] = int(row[2])
        
        # another user or another month
        if userID != curAnsRow[0] or month != curAnsRow[1]:
            # update the last month data to answer list
            answerTab.append(curAnsRow)
            # clear the current insight data
            curAnsRow = [userID, month, row[2], row[2], row[2]]
        
        # same month data
        else:
            # update max, min and current balance
            curBalance = curAnsRow[4] + row[2]
            curAnsRow[2] = min(curAnsRow[2], curBalance)
            curAnsRow[3] = max(curAnsRow[3], curBalance)
            curAnsRow[4] = curBalance 
 
    answerTab.append(curAnsRow)
    # write the data into new file
    with open('output.csv', 'w+', newline ='') as csvfile:   
        write = csv.writer(csvfile)
        write.writerows(answerTab[1:])
            
            
def main():
    """
    Main function to analyze the transactions.
    
    """
    
    # Remove the first argument
    argumentList = sys.argv[1:]
    
    # Long options
    long_options = ["FileName="]
 

    # Options
    options = "f:"
    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking argument
        if len(arguments) == 0:
            print("Lack of file name argument")

        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-f", "--FileName"):

                # file exist
                if os.path.exists(currentValue):
                    data = inputProcess(currentValue)
                    dataAnalyze(data)
                    print ("Analyze done.")
                    
                # file doesn't exist
                else:
                    print ("File doesn't exist.")

            # Wrong augument
            else:
                print("Wrong argument")
                
    except getopt.error as err:
        # Output error, and return with an error code
        print (str(err))
    

if __name__ == "__main__":
    main()
    