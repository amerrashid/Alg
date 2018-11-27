# { }
provinces = {'qc': 'Quebec', 'on': 'Ontario', 'bc': 'British Colombia'}

print(provinces.keys())
print(provinces.items())
for k,v in provinces.items():
    print(k,v)
for a,b in provinces.items():
    print(b)

inp = ""
prov = input ("Enter the province code: ")

# if prov in provinces:
#     result = provinces[prov.lower()]
#     print("The province name is {0} ".format(result))
# else:
#     print("Sorry the province code is not recognized")


try:
    result = provinces[prov.lower()]
    print("The province name is {0} ".format(result))
except KeyError:
    print("Sorry the province code is not recognized")

