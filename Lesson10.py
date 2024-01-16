# Написати валідації за допомогою регулярних виразів та протестувати
# на рiзних кейсах:
# - домашній номер телефону (тільки цифри та довжина номера)
#
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
#
# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та
#          максимальна на ваш вибір)
#
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
#
# додатково:
#
# - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра,
#           один символ, довжина пароля – від 8 до 16 символів)

import re

# - домашній номер телефону (тільки цифри та довжина номера)
phone_numbers1 = ["1234567", "123456", "7654321", "420510384", "89589892115"]
print(phone_numbers1)
for phone_number in phone_numbers1:
    if re.match(r'^\d{7}$', phone_number):
        print(f"number {phone_number} valid")
    else:
        print(f"number {phone_number} invalid")

# Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
phone_numbers2 = ["+38099123456789", "380991234567", "+38099123456","+420199188177166", "!420199188177166", "420728485231"]
print(phone_numbers2)
for phone_number in phone_numbers2:
    if re.match(r'^\+?\d{12}$', phone_number):
        # 12 цифр для повного номеру моб телефону, 9 цифр без коду країни
        print(f"number {phone_number} valid")
    else:
        print(f"number {phone_number} invalid")

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина
# та максимальна на ваш вибір)

emails = ["rostyslav.ushakov@gmail.com", "rostyslav_ushakov@gmail.com", "rostyslav-ushakov@gmail.com", "rostyslavushakov@gmailcom",
          "ushakovgmailcom", "rostyslavushakovgmail.com", "11rostyslav.ushakov@gmail.com"]

for email in emails:
    if re.match(r"^[a-zA-Z0-9]+[._-]?[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", email):
        print(f"email {email} valid")
    else:
        print(f"email {email} invalid")

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
fio = "Rostyslav Rostyslavovych Ushakov"
if re.match(r'^[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}$', fio):
    print("Correct")
else:
    print("Incorrect")

