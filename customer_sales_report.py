import csv
import pandas as pd

sales_report = open('salesreport.csv', 'w')
df = pd.read_csv('sales.csv', delimiter=',')
sales_report.write("Customer, Total\n")


for i in range(250, 262):
    total = 0
    for record in df.index:
        if df['CustomerID'][record] == i:
            total = total + float(df['SubTotal'][record]) + \
                float(df['TaxAmt'][record]) + float(df['Freight'][record])
    total = round(total, 2)
    sales_report.write(f"{i}, {total}\n")
