import csv

with open('budget_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header = next(readCSV)
    # print(len(readCSV))
    i =0
    previous_value = 0 
    monthly_change = []
    total_current_change =0
    total = 0
    Smallest_change = [] 
    Largest_change = []
    for row in readCSV:
        if i ==0:
            Smallest_change = [row[0],row[1]]
            Largest_change = [row[0],row[1]]
            previous_value = int(row[1])
            #print(previous_value)
        else:
            current_change = int(row[1]) - previous_value
            #print(current_change)
            if current_change < float(Smallest_change[1]):
                Smallest_change = [row[0],current_change]
            if current_change > float(Largest_change[1]):
                Largest_change = [row[0],current_change]
            monthly_change.append([row[0],current_change])
            total_current_change =  total_current_change + current_change
            previous_value = int(row[1])
        #print(row[1])
        i = i+1
        #print(int(row[1]))
        total = total + int(row[1])
    monthly_mean = total_current_change / (i-1)
    output =""
    output = output+"\n"+'The total number of months in the data is ' + str(i)
    output = output+"\n"+'The net profit/ loss is $' + str(total)
    output = output+"\n"+'The mean monthly profit/ loss is $'+ str(int(monthly_mean))
    output = output+"\n"+'The greatest monthly increase in profits was on ' + str(Largest_change[0]) + ' and it was $'+ str(Largest_change[1])
    output = output+"\n"+'The greatest monthly decrease in profits was on '+ str(Smallest_change[0]) + ' and it was $'+ str(Smallest_change[1])
    print(output)
    #print('The total number of months in the data is ' + str(i))
    #print('The net profit/ loss is $' + str(total))
    #print(monthly_change)
    #print(total_current_change)
    #print('The mean monthly profit/ loss is $'+ str(int(monthly_mean)))
    #print('The greatest monthly increase in profits was on ' + str(Largest_change[0]) + ' and it was $'+ str(Largest_change[1]))
    with open('PyBank.txt', 'w') as txt:
            txt.write(output)