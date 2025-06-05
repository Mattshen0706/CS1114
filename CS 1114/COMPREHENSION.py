# Example problem 1:
# create a list of squares of even numbers from 1 to 20 

# squareeven=[num**2 for num in range(1,21) if num%2==0]

# print(squareeven)


# Example problem 2:
# filter only strings from a list and convert them to uppercase

# itemlist=[1,2,3,"words","hello",124,"world"]
# filteredlist=[item.upper() for item in itemlist if type(item)==str]

# print(filteredlist)


# Example problem 3:
# make a 2d list into a 2d list
# list2d=[[1,2,3],[4,5,6],[7,8,9]]
# list1d=[sublist for list in list2d for sublist in list]

# print(list1d)


# original= {'A':1,"B":2,"C":3}
# inverted={v:k for k, v in original.items()}
# print(original)
# print(inverted)

# Example problem 4:
# Unpacking values in a list of list:
# countries=[("China","Shanghai"),("Mexico","Mexico City"),("USA","Washington DC"),("France","Paris")]
# countrydict={country:capital for country, capital in countries}
# print(countrydict)

# In order to unpack this way every element in the 2 dimensional list must be the same lenght


NUMBER_LIST=[4,5,6,7,9,10,13,15,20,45,50,80]
VEHICLES_DICT={"SEDAN":1500,
               "SUV":2000,
               "Pickup":2500,
               "Minivan":1600,
               "Van":2400,
               "Semi":13600,
               "Bicycle":7,
               "Motorcycle":110}
 
1. 
new_list = [num+5 for num in NUMBER_LIST]
square_list=[num**2 for num in NUMBER_LIST if num**2<50]
custom_list=[num for num in NUMBER_LIST if num<50 and num%5==0 and num%3==0]
new_vehicle_list=[vehicle for vehicle, mass in VEHICLES_DICT.items() if 2000<mass<3000]

print(new_list)
print(square_list)
print(custom_list)
print(new_vehicle_list)
