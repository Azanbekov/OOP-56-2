from faker import Faker

fake = Faker()

print("Имя:", fake.name())
print("Адрес:", fake.address())
print("Email:", fake.email())
print("Телефон:", fake.phone_number())