import csv

filename = "pc.csv"
filepath = "../csv"

def writetocsv(path):
    fields = ["pc_name", "ip"]
    rows = []

    address = [172, 30, 2, 1]

    for i in range(0, 100):
        rows.append(
            {"pc_name": f"P{address[3]}", "ip": f"{address[0]}.{address[1]}.{address[2]}.{address[3]}"}
        )
        address[3] += 1

    with open(path, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

        reader = csv.reader(csvfile)

writetocsv(f"{filepath}/{filename}")