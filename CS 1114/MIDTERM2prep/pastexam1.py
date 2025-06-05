# PROBLEM 1:

# var=b

# var=abab

# var=fd

# var=f

# var=[1,2,3]

# ERROR (List object only has index function)

# var=3

# ERROR (can not concactanete list and string)

# var=["ab","cd"]

# var=3


# PROBLEM 2:

# def first_func(a):
# print("first 1:",a)
# a = a*2 
# print("first 2:",a);

# def second_func(a,b):
# print("Second 1:",a,b)
# first_func(a)
# print("Second 2:",a,b)
# first_func(b)
# print("Second 3:",a,b)
# a.append(3)
# b=5

# def main():
# print("Main 1")
# ls = [1,2]
# x=5
# second_func(ls,x)
# print("Main 2: ",ls,x)

# if __name__=='__main__':
# main();

# ls=[1,2]
# x=5

# Main 1
# Second 1: [1,2] 5
# first 1: [1,2]
# first 2: [1,2,1,2]
# Second 2: [1,2] 5
# first 1: 5
# first 2: 10
# Second 3: [1,2] 5
# Main 2: [1,2] 5

# PROBLEM 3:

# a) None
# b) Error (tandon allows for no arguements) 
# c) list
# d) list
# e) list


# PROBLEM 4:

# File 1: player_one_stats.csv
# Character Name,Attack Power,Health Points
# Ash's Pikachu,15,100

# File 2: player_two_stats.csv
# Character Name,Attack Power,Health Points
# Gary’s Eevee,17,90

with open("player_one_stats.csv","w") as writefile:
    print("Character Name,Attack Power,Health Points",file=writefile)
    print("Ash's Pikachu,15,100",file=writefile)
    
with open("player_two_stats.csv","w") as writefile:
    print("Character Name,Attack Power,Health Points",file=writefile)
    print("Gary’s Eevee,17,90",file=writefile)
    
import random

def load_character(characterfile):
    characterlist=[]
    try:
        with open(characterfile,'r') as readfile:
            line1=readfile.readline()
            line2=readfile.readline()
            characterstring1=line2
            strippedstring=characterstring1.strip()
            characterlist=strippedstring.split(',')
            return characterlist
    except:
        return characterlist

def battle(character1,character2):
    if character1==[] or character2==[]:
        return "NO CONTEST"
    else:
        winner="" 
        character1attack=int(character1[1])
        character1health=int(character1[2])
        character2attack=int(character2[1])
        character2health=int(character2[2])  
        while character1health>=0 and character2health>=0:
            hitrate1=random.randint(0,10)
            hitrate2=random.randint(0,10)
            if hitrate1<=7:
                character2health-=character1attack         
                if character2health<0:
                    winner=character1[0]
                else:
                    if hitrate2<=7:
                        character1health-=character2attack 
                    if character1health<0:
                        winner=character2[0]
                    
        return winner
            


def main():
    pikachu = load_character("player_one_stats.csv")
    eevee = load_character("player_two_stats.csv")
    winner = battle(pikachu, eevee)
    print(winner) 
    # Prints either "Ash's Pikachu", "Gary's Eevee", or # “NOCONTEST”

main()


# PROBLEM 5:

# [“Product Name”, ”Product Description”, “Barcode”, price]
# All products will have all 4 items (3 strings and 1 float) in their list and the lists will be
# stored in a larger list (products) which represents all of the products in the store.

productlist=[["Tomatoes","NNN","SS1",54.25],["Cucumbet","NNN","SS2",5.5],["Jackfruit","NNN","SS3",20]]
buyerlist=["SS1","SS2","SS3","SS4"]
def get_item(productlist,barcode):
    position=""
    emptylist=[]
    for i in range(0,len(productlist)):
        if barcode == productlist[i][2]:
            return productlist[i]
    return emptylist
           
def get_basket_cost(productlist,buyerlist):
    total_cost=0
    for items in buyerlist:
        itemdata=get_item(productlist,items)
        if itemdata==[]:
            total_cost+=1000000
        else:
            total_cost+=itemdata[-1]
    print(total_cost)
        
get_basket_cost(productlist,buyerlist)

# PROBLEM 6:
with open("contest_data.txt","w") as writefile:
    print("Luca,Pizza,5\nGiulia,Gelato,2\nMatteo,Pasta,7\nLuca,Pasta,4\nLuca,Gelato,2\nGiulia,Pizza,2",file=writefile)
    
def load_contest_data(filename):
    newlist=[]
    try: 
        with open(filename,"r") as readfile:
            for lines in readfile:
                newline=lines.strip()
                newlinelist=newline.split(',')
                newlist.append(tuple(newlinelist))
            return(newlist)  
    except FileNotFoundError:
        return newlist

def get_totals_eaten(data,names):
    newlist=[]
    food_intake=0
    for name in names:
        for items in load_contest_data(data):
            if name==items[0]:
                food_intake+=int(items[2])
        newlist.append((name,food_intake))
        food_intake=0
    return newlist

def get_winner(totals):
    eatamount=[]
    winner=""
    for i in range (0,len(totals)):
        eatamount.append(totals[i][1])
    maxvalue=max(eatamount)
    indexvalue=eatamount.index(maxvalue)
    winner=totals[indexvalue]
    print(winner)
    
get_winner(get_totals_eaten("contest_data.txt",["Luca", "Giulia","Marie"]))
   
