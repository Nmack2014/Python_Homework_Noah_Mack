import os, csv

budget_csv = os.path.join('Resources', 'budget_data.csv')
a = 0
total_profit = int()
change = int()
total_change = int()
max_val = int()
max_ele = int()
min_val = int()
min_ele = int()
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = list(csv_reader)
    data.pop(0)
   
    for a in range(len(data)):
        total_profit = total_profit + int(data[a][1]) 
        change = int(data[a][1]) - int(data[a-1][1])
        if max_val < change:
            max_val = change
            max_ele = a 
        if min_val > change:
            min_val = change
            min_ele = a 
        a += 1
        
        

total_change = int(data[len(data)-1][1]) - int(data[0][1])
        


            

print("Financial Analysis")
print("__________________")
print("Total Months: ", len(data))
print("Total Profit: $", total_profit)
print("Average Change:", (total_change / (len(data)-1)))
print("Greatest Increase in Profits:", data[max_ele][0],"($",max_val,")")
print("Greatest Decrease in Profits:", data[min_ele][0],"($", min_val,")")

