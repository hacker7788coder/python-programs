customer = {
    "name":  "Vasu Gajera",
    "age":18,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))
customer = {
    "name":  "Vasu Gajera",
    "age":18,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])