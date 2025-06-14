
# Recursive Tree:


Each recursive call is represented as a node in the tree. Inside each node, we write the size of the input it was called with 

If A directly calls B, we draw an edge from the node representing A to the node representing B 

At the side of each node, we write the local cost of that recursive call without including the cost of the recursive call it makes 

Sum of all the local costs will equal to the total cost of the recursive function 



# Activation Record: 
### Everytime you make a function call it contains 4 things:
            - Parameters
            - Space for Local Variables
            - Return Point in the Code 
            - Space for the return value

You should be able to follow all the function calls down the call stack 

Stack overflow: when you don't include a base case in the recursive function, resulting in an infinite loop

| Paramters| Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |

