import csv

pay_file = open('EmployeePay.csv', 'r')
pay_reader = csv.reader(pay_file, delimiter=',')
next(pay_reader)

for i in pay_reader:
    totalpay = int(i[3])*float(i[4])+int(i[3])
    print(f"The employee {i[1]} {i[2]} has a total pay of ${totalpay}")
    input()
