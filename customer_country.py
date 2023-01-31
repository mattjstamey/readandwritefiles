import csv

customer_file = open('customers.csv', 'r')
customer_reader = csv.reader(customer_file, delimiter=',')
customer_country = open('customer_country.csv', 'w')
next(customer_reader)
n = 0
for i in customer_reader:
    customer_country.write(f"{i[1]},{i[2]},{i[4]}\n")
    n += 1

print("The total number of customers read from the file was", n)

customer_country.close()
customer_file.close()
