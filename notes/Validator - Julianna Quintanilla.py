import csv

# test_num = "4556737586899855"


def validate(num: str):
    if len(num) == 16:
        last_num = int(num[15])
        list_form = list(num)
        list_form.pop(15)
        reversed_form = list_form[::-1]
        print(reversed_form)
        for index in range(len(reversed_form)):

            return False


# print(validate(test_num))

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print("OK")
