import csv

def check_stock():
    restock = []

    # open the csv file
    with open("stock.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                name = row["item_name"]
                qty = int(row["current_quantity"])
                limit = int(row["reorder_threshold"])

                if qty < limit:
                    if qty < 0.25 * limit:
                        status = "Critical"
                    else:
                        status = "Low"
                    reorder = limit * 2 - qty
                    restock.append([name, qty, limit, status, reorder])
            except:
                # skip bad rows
                continue

    # print report
    print("Restock Needed:")
    for item in restock:
        print(item[0], "Qty:", item[1], "Limit:", item[2],
              "Status:", item[3], "Reorder:", item[4])

    # write to new csv
    with open("restock_report.csv", "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["item_name", "current_quantity", "threshold", "status", "suggested_reorder"])
        writer.writerows(restock)

check_stock()
