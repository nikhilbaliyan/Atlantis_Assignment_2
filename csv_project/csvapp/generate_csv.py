import csv
from faker import Faker
from random import randint


def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            processed_full_name = full_name.split(" ")
            first_name = processed_full_name[0]
            last_name = processed_full_name[1]
            domain_name = "@testDomain.com"
            userId = first_name + "." + last_name + domain_name

            writer.writerow({
                "id": randint(1, 10000),
                "email": userId,
                "first_name": first_name,
                "last_name": last_name,
                "Pincode": fake.zipcode(),
                "timestamp": fake.date_time(),
            })


if __name__ == '__main__':
    records = 10000
    headers = ["id", "first_name", "last_name", "email", "Pincode", "timestamp"]
    datagenerate(records, headers)
    print("CSV generation complete!")
