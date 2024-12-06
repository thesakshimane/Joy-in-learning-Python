from tabulate import tabulate

'''
This script generates a magic square, which is a square matrix of size nxn where the sum of every row, column, and diagonal is the same. The program implements the Siamese method (used for odd-sized magic squares).
'''

def setup_variables():
    """
    Prompt the user to input the size of the magic square (n).
    """
    n = int(input("Please enter the value of n which is the order of the magic square nxn: "))
    ms = [[None for _ in range(n)] for _ in range(n)]
    return n, ms

def generate_magic_square(n, ms):
    """
    Generates the magic square using the Siamese method.
    
    Args:
        n (int): The order of the magic square.
        ms (list): A 2D list initialized with None to store the magic square.
    """
    p = n//2
    q = n-1
    ms[p][q] = 1
    i = 2
    while (i <= n*n):
        p -= 1
        q += 1
        if p == -1 and q == n:
            p = 0
            q = n-2
        elif p == -1:
            p = n-1
        elif q == n:
            q = 0
        elif ms[p][q] != None:
            p += 1
            q -= 2
        if ms[p][q] == None:
            ms[p][q] = i
        i += 1
    

def display(ms):
    """
    Displays the magic square in a formatted grid using the tabulate module.
    
    Args:
        ms (list): A 2D list containing the magic square.
    """
    print(tabulate(ms, tablefmt="grid"))
    return ms

if __name__ == "__main__": 
    n, ms = setup_variables()
    generate_magic_square(n , ms)
    display(ms)