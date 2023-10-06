import csv
import os
from datetime import datetime

def generate_csv():
    # Set up the headers and initial data
    headers = ["key", "table_type", "column_type"]
    data = [
        ["TestDataSource.public", "", ""],
        ["TestDataSource.public.customers", "TABLE", ""],
        ["TestDataSource.public.orders", "TABLE", ""],
        ["TestDataSource.public.largeTable", "TABLE", ""],

        ["TestDataSource.public.customers.customerID", "", "int"],
        ["TestDataSource.public.customers.firstName", "", "varchar(255)"],
        ["TestDataSource.public.customers.lastName", "", "varchar(255)"],
        ["TestDataSource.public.customers.email", "", "varchar(255)"],
        ["TestDataSource.public.customers.phone", "", "varchar(20)"],
        ["TestDataSource.public.customers.address", "", "varchar(255)"],
        ["TestDataSource.public.customers.city", "", "varchar(255)"],
        ["TestDataSource.public.customers.state", "", "varchar(2)"],
        ["TestDataSource.public.customers.zipCode", "", "varchar(10)"],

        ["TestDataSource.public.orders.orderID", "", "int"],
        ["TestDataSource.public.orders.customerID", "", "int"],
        ["TestDataSource.public.orders.orderDate", "", "date"],
        ["TestDataSource.public.orders.shippingDate", "", "date"],
        ["TestDataSource.public.orders.shippingAddress", "", "varchar(255)"],
        ["TestDataSource.public.orders.totalAmount", "", "float"],
        ["TestDataSource.public.orders.status", "", "varchar(50)"]
    ]

    # Add largeTable columns
    for i in range(1, 501):
        data.append([f"TestDataSource.public.largeTable.column{i}", "", "varchar(255)"])

    # Create an output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Get today's date and format the filename
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f"alation_fake_metadata_{today}.csv"
    filepath = os.path.join(output_dir, filename)

    # Write data to a CSV file
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"CSV file has been written to '{filepath}'")

if __name__ == "__main__":
    generate_csv()
