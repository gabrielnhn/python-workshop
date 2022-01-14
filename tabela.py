import csv

with open("./capcom_cup.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ANO", "CAMPEAO"])
    writer.writerow(["2016", "NuckleDu"])
    writer.writerow(["2017", "MenaRD"])
    writer.writerow(["2018", "Gachikun"])
    writer.writerow(["2019", "iDom"])

# with open("./capcom_cup.csv", "r") as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)