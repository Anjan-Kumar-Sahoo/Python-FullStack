names = ["Maruti Suzu","BMW","Mercedes Benz","Tata","Hyundai","Kia","Toyota","Honda","Nissan","MG Motors"]

print("Names with length greater than 4:")
names4 = list(filter(lambda name: len(name) > 4, names))
list(map(print, names4))

print("All names in uppercase:")
upper_names = list(map(lambda name: name.upper(), names))
list(map(print, upper_names))