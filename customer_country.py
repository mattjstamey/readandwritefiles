import csv

customer_file = open('customers.csv','r')
customer_country = csv.reader(customer_file,delimiter=',')
next(customer_file)

for i in customer_file:
    print(i[0])


customer_file.close()

