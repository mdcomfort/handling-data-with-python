open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     print(line)

# for line in open_file:
#     line = line.split(",")
#     cupcake_type = line[2]
#     print(cupcake_type)

for line in open_file:
    line = line.split(",")
    quantity = int(line[3])
    price = float(line[4])
    line_total = quantity * price
    print(line_total)


invoice_total = 0

for line in open_file:
    line = line.split(",")
    quantity = int(line[3])
    price = float(line[4])
    line_total = quantity * price
    invoice_total += line_total

print(invoice_total)      


