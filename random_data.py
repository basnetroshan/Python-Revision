import random

first_names = ["Roshan", "Subir", "Nikesh", "Prabin", "Rahul", "Sean", "Nipuni", "Awanti", "Pasandi", "Ashiq", "Xiao", "Sagar", "Sulav", "Santosh", "Dinesh", "Jaspreet", "Pasandi", "Yu-yun", "Mayu"]

last_names = ["Basnet", "Zhan", "Singh", "Upadhyaya", "Yeh", "Rahman", "Chhetri", "Karm", "Maharjan", "Shrestha", "Manawadhu", "Bajracharya", "Acharya", "Aryal", "Kunwar", "Pandey", "Khatri", "Budhathoki"]

street_names = ["Sasukhwat", "Bageshwori", "Gladstone", "Hubert", "Flinders Lane", "Collins", "Elizabeth", "Austin Terrace", "De Carle", "Manohara", "Albion", "Glenhuntly", "lakeside Drive", "Pine", "cider"]

fake_cities = ["Kathmandu", "Melbourne", "Glenroy", "Moone Ponds", "South Yarra", "Pokhara", "Butwal", "Chitwan", "Hetauda", "Brisbane", "Albion", "Warrambol", "Lorne", "Appolo Bay", "Prahan", "Sydney", "Bhojpur"]

states = ["VIC", "KTH", "SYD", "BSB", "PKR", "BTW", "CHT", "ADE", "PTH", "DAR", "OAK", "IDE", "OKO", "TBE", "CRC", "ZVZ", "RMR" ]

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(1000, 9999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@olamail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')