import csv

# Function to categorize sales into ranges
def sales_range(sales):
    ranges = {
        "0-5": 0,
        "5-10": 0,
        "10-20": 0,
        "20-30": 0,
        "30-40": 0,
        "40-50": 0,
        "50+": 0
    }

    for sale in sales:
        if 0 <= sale < 5:
            ranges["0-5"] += 1
        elif 5 <= sale < 10:
            ranges["5-10"] += 1
        elif 10 <= sale < 20:
            ranges["10-20"] += 1
        elif 20 <= sale < 30:
            ranges["20-30"] += 1
        elif 30 <= sale < 40:
            ranges["30-40"] += 1
        elif 40 <= sale < 50:
            ranges["40-50"] += 1
        elif sale >= 50:
            ranges["50+"] += 1

    return ranges

# Function to read the CSV file and extract the "Net Sale" column
def read_sales_data(filename):
    sales = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for i, row in enumerate(csv_reader):
            try:
                net_sale = row['Net Sale'].strip()
                if net_sale:
                    sales.append(float(net_sale.replace('$', '').replace(',', '')))
            except ValueError:
                print(f"Invalid data found in row {i+1}: {row}")
            except KeyError:
                print(f"Column 'Net Sale' not found in row {i+1}: {row}")
    return sales

# Main function to process sales data
def main():
    filename = '05_2024 Sales.csv'
    sales = read_sales_data(filename)
    if not sales:
        print("No valid sales data found.")
        return

    print(f"Total number of sales entries read: {len(sales)}")

    categorized_sales = sales_range(sales)

    # Find the most popular range
    most_popular_range = max(categorized_sales, key=categorized_sales.get)
    most_popular_count = categorized_sales[most_popular_range]

    # Print the results
    print("Sales categorized by range:")
    total_sales_count = 0
    for range_, count in categorized_sales.items():
        print(f"{range_}: {count}")
        total_sales_count += count

    print(f"\nMost popular range: {most_popular_range} with {most_popular_count} sales")
    print(f"Total sales count: {total_sales_count}")

if __name__ == '__main__':
    main()
