from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Nokia", "A22", "+79131597534."))
catalog.append(Smartphone("Apple", "iPhone 17", "+79505462424"))
catalog.append(Smartphone("Xiaomi", "Redmi 15F", "+79023337788"))
catalog.append(Smartphone("Samsung", "S27", "+79831596678"))
catalog.append(Smartphone("Techo", "Pova 8", "+79835467878"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")