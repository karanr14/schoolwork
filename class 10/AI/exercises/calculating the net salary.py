## calculate net salary
## net salary = basic salary + HRA + DA-PF
## HRA = 30% of basic | DA = 20% of basic  | PF = 12% of basic

basic_sal=float(input("Enter the basic salary: "))
HRA = basic_sal * 0.30
DA = basic_sal * 0.20
PF = basic_sal * 0.12
net_sal = basic_sal + HRA + DA - PF

print(f"The net salary is {net_sal}")