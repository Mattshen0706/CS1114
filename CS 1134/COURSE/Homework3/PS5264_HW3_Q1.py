import ctypes;

def makearray(n):
    return (n * ctypes.py_object)();

class ArrayList:
    def __init__(self):
        self.data=makearray(1);
        self.capacity=1;
        self.num_of_elements=0;

    def __len__(self):
        return self.num_of_elements;

    def append(self, item):
        if (self.num_of_elements==self.capacity):
            self.resize(self.num_of_elements*2);
        self.data[self.num_of_elements] = item;
        self.num_of_elements+=1;

    def pop(self, position=-1):

        if position<=-1:
            position+=self.num_of_elements
        if position==-1 and self.num_of_elements>0: # Theta (1)
            #self.resize(self.num_of_elements-1);
            temp = self.data[self.num_of_elements];
            self.data[self.num_of_elements-1]=None; #cybersecurity?????
        elif 0<=position<self.num_of_elements: #Theta(n)
            temp = self.data[position];
            for i in range(position,self.num_of_elements-1):
                self.data[i] = self.data[i+1];
        else:
            raise IndexError();

        self.num_of_elements-=1;
        if self.num_of_elements<self.capacity*0.25:
            self.resize(self.capacity//2)
        return temp;
        
    def extend(self, iterable):
        size=len(iterable);
        if (self.num_of_elements+size)>self.capacity:
            self.resize(self.num_of_elements+size);
        for item in iterable:
            self.append(item);
        
    def resize(self, newsize):
        newarray = makearray(newsize);

        #copy over the elements
        if (newsize>self.num_of_elements): #new size is larger
            for i in range(self.num_of_elements):
                newarray[i] = self.data[i];
        else: #new size is smaller, not all elements will fit.
            for i in range(newsize):
                newarray[i] = self.data[i];
            self.num_of_elements=newsize;
        self.data = newarray; # not a copy, just an alias
        self.capacity=newsize;

    def __getitem__(self,index):
        if (index<0):
            index+=self.num_of_elements;
        if (0<=index<self.num_of_elements):
            return self.data[index];
        raise IndexError("Invalid Index");

    def __setitem__(self, index, value):
        if (index<0):
            index+=self.num_of_elements;
        if (index<0 or index>=self.num_of_elements):
            raise IndexError("list assignment index out of range");
        self.data[index] = value;
    def index(self, value):
        index = 0;
        while (index<self.num_of_elements):
            if self.data[index] == value:
                return index;
            index+=1;
        raise ValueError(value+" is not in the list");
    def remove(self, value):
        self.pop(self.index(value));
    def count(self, value):
        times =0;
        for i in self:
            if i==value:
                times+=1;
        return times;
    def insert(self, index, value):
        self.append(None);
        if (index<0):
            index+=self.num_of_elements;
        if (index<0 or index>=self.num_of_elements):
            raise IndexError("list assignment index out of range");
        for i in range(self.num_of_elements-1, index,-1):
            #self.data[i],self.data[i-1] = self.data[i-1],self.data[i];
            self.data[i] = self.data[i-1];
        self.data[index] = value;
    def clear(self):
        self.data=makearray(1);
        self.capacity=1;
        self.num_of_elements=0;
    def copy(self):
        temp = ArrayList();
        temp.extend(self);
        return temp;
    def __str__(self):
        s="["
        for i in range(0,self.num_of_elements-1):
            s+=(str(self.data[i])+',')
        s+=(str(self.data[-1+self.num_of_elements]))
        s+=("]")
        return s
        
    
def main():
    arr_lst = ArrayList() 
    for i in range(1, 4+1):
        arr_lst.append(i)
    arr_lst.insert(0, 30)
    arr_lst.pop(-2)
    print(arr_lst)

    # ls.append(100);
    # print(ls[0]);
    # ls[0] = 200;
    # print(ls[0]);
    # ls.append(300);
    # ls.append(400);
    # ls.append(500);
    
    # size = len(ls);
    # print(size);

    
    
if __name__=='__main__':
    main();














