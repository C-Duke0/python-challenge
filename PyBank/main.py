import os
import csv

# Define the path to CSV:
file_path = '/Users/christopherduke/python-challenge/PyBank/Resources/budget_data.csv'

# Set lists:
total_months = []
total_pl = []


# Open the CSV 
with open(file_path) as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)



    # Read the header row
    csv_header = next(csv_reader)
    
    #loop through each row in CSV
    for rows in csv_reader:
        total_months.append(rows[0])
        total_pl.append(int(rows[1]))

# set differences between month profits/losses
diff = [total_pl[i+1] - total_pl[i] for i in range(len(total_pl)-1)]    
# add differences
total_pl_sum = sum(total_pl)
# find the average of the differences, rounded
total_a = round(sum(diff)/len(diff))
# calculate max and min
max_inc = max(diff)
max_dec = min(diff)

# find the index of the value for the max increase and decrese in row 1
max_inc_value = diff.index(max_inc) 
max_dec_value = diff.index(max_dec)

# Find the month that corresponds with the previous values. Add one to find the month of change in profits
max_inc_month = total_months[max_inc_value + 1]
max_dec_month = total_months[max_dec_value + 1]

    

print ("Financial Analysis")
print ("---------------------")
print("Total Months: " + str(len(total_months)))
print ("Total: " + str(total_pl_sum))
print ("Average Change: " + str(total_a))
print (f"Greatest increase in profits:  {max_inc_month} (${max_inc})")
print (f"Greatest decreatse in profits: {max_dec_month} (${max_dec})")

#create text file
output_file = '/Users/christopherduke/python-challenge/PyBank/analysis/financial.txt'
with open(output_file, "w") as file:
    
    #specify what to write
    file.write("Financial Analysis")
    file.write(("\n"))
    file.write("---------------------")
    file.write(("\n"))
    file.write("Total Months: " + str(len(total_months)))
    file.write(("\n"))
    file.write("Total: " + str(total_pl_sum))
    file.write(("\n"))
    file.write("Average Change: " + str(total_a))
    file.write(("\n"))
    file.write(f"Greatest increase in profits:  {max_inc_month} (${max_inc})")
    file.write(("\n"))
    file.write(f"Greatest decreatse in profits: {max_dec_month} (${max_dec})")
    
