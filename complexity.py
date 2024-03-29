from random import randint
from binarysearchtree import BinarySearchTree
import time
import matplotlib.pyplot as plt
import math
import sympy as sym
from linkedlist import LinkedList

##Global Variables##
TREE_SIZE = 101
NUMBER_OF_TREES = 500

#Function to Gererate n Binary Search Trees populated with values between 1 and 1000#
def random_tree(n):
    bst = BinarySearchTree()
    for _ in range(n):
        insert_val = randint(1,1000)
        bst.insert(insert_val)
    return bst

#Function to Gererate n LinkedLists populated with values between 1 and 1000#
def random_llist(n):
    llist = LinkedList()
    for _ in range(n):
        insert_val = randint(1,1000)
        llist.insert(insert_val)
    return llist

def main():
    X = [x for x in range(5,TREE_SIZE) if x % 5 == 0]
    Y = []
    #Generate Binary Search Trees and Searching for the number 42 in each tree, then append the time taken to Y
    for s in X:
        timings = []
        for _ in range(NUMBER_OF_TREES):
            bst = random_tree(s)
            start_time = time.time()
            bst.search(42)
            total_time = time.time() - start_time
            timings.append(total_time)
        avg_time = sum(timings)/len(timings)
        Y.append(avg_time)
        
    Y4 = []
    #Generate LinkedLists and Searching for the number 42 in each tree, then append the time taken to Y4
    for s in X:
        timings_llist = []
        for _ in range(NUMBER_OF_TREES):
            llist = random_llist(s)
            start_time = time.time()
            llist.search(42)
            total_time = time.time() - start_time
            timings_llist.append(total_time)
        avg_time = sum(timings_llist)/len(timings_llist)
        Y4.append(avg_time)
    
    # Using sympy to compute seet of linear equations to find the constants of the equation
    x,y = sym.symbols('x,y')
    t = Y[0]
    t2 = Y[1]
    #Equations for linear time estimation
    eq1 = sym.Eq(x*5+y,t)
    eq2 = sym.Eq(x*10+y,t2)
    result1 = sym.solve([eq1,eq2],(x,y))
    #Equations for log time estimation
    eq1 = sym.Eq(sym.log(5,2)*x+y,t)
    eq2 = sym.Eq(sym.log(10,2)*x+y,t2)
    result2 = sym.solve([eq1,eq2],(x,y))

    #outputting estimated times to list Y2 and Y3 using computed constants
    c2 = result1[sym.symbols('x')]
    b2 = result1[sym.symbols('y')]
    Y2 = [c2*x + b2 for x in range(5,101) if x % 5 == 0]

    c3 = result2[sym.symbols('x')]
    b3 = result2[sym.symbols('y')]
    Y3 = [c3*math.log(x,2) + b3 for x in range(5,101) if x % 5 == 0]

    # Complexity analysis X vs Y#
    # From the graph using the time module for the timing, the complexity appears to be running in mostly O(n) or linear time
    # It initially appears to follow a log(n) path as expected
    # However it displays a positive linear relationship (n) as tree size increases
    ## 2.4.4
    plt.plot(X, Y)
    plt.legend(['BST'])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.show()

    # Complexity analysis X vs Y, Y2 and Y3#
    # From the graph using the time module for the timing, the complexity appears to be running in mostly O(log(n)) or logarithmic time
    # It closely follows the log(n) predicted path, or oscillates around it.
    # As the numbers are inserted randomly a too low seed node or too high seed as the root will unbalance the tree towards the right or left
    # respectively. Ideally we should generate the whole list we'd like to insert and set the median value as the root, to get the most balanced tree.
    # Subsequent nodes should still be added in random, this would result in a more accurate log(n) path.
    ## 2.4.6
    plt.plot(X, Y)
    plt.plot(X, Y2)
    plt.plot(X, Y3)
    plt.legend(['BST','Linear','Logarithmic'])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.show()

    # Complexity analysis X vs Y, Y2, Y3 and Y4#
    # From the graph using the time module for the timing, the BST complexity appears to be running in mostly O(log(n)) or logarithmic time
    # Meanwhile from the graph, the LinkedList complexity appears to be running in mostly O(n) or linear time
    # As each node has to be traversed once in a linked list it travserses it in n time
    # Meanwhile BST can potentially half the nodes to be search after each iteration assuming the tree is balanced, thus reesulting in logn time
    ## 2.7
    plt.plot(X, Y)
    plt.plot(X, Y2)
    plt.plot(X, Y3)
    plt.plot(X, Y4)
    plt.legend(['BST','Linear','Logarithmic', 'LinkedList'])
    plt.xlabel('Size of trees')
    plt.ylabel('Search time')
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.show()
    
if __name__ == "__main__":
    main()