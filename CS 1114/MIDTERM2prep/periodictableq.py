def load_function():
    periodic=[]
    try:
        with open('MIDTERM2prep/chem_data.txt',"r")as readfile:
            firstline=readfile.readline  
            for lines in readfile:
                newline=lines.strip("\n,[ ]")
                linelist=newline.split(",")
                modifiedlist=[]
                for elements in linelist:
                     newelement=elements.strip('" "')
                     modifiedlist.append(newelement)
                periodic.append(modifiedlist)
                # print(newline)
            popped=periodic.pop(0)
            popped2=periodic.pop(-1)
            return periodic
    except FileNotFoundError:
            print("File does not exist")

def average(periodic):
    sum=0
    count=0
    for elements in periodic:
        sum+=float(elements[3])
        count+=1
    average =sum/count
    return average

def longest_name(periodic):
    prev=0
    newlist=[]
    for elements in periodic:
        if len(elements[0])>prev and len(elements[0])<12:
            newlist=[]
            newlist.append(elements[0])
            prev=len(elements[0])
        elif len(elements[0])==prev:
            newlist.append(elements[0])
    return newlist
              

def main():
    periodictable=load_function()
    # print(periodictable)
    print(f'{average(periodictable):.2f}')
    print(longest_name(periodictable))


main()