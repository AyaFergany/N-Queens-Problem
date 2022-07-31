# Function backtracking_checker => checks is last element breaks the pattern or not
# Parameters:
# p => partial solution

def backtracking_checker(p):
    i=len(p)-1
    for j in range(i):
        if( i-j == abs(p[i]-p[j])):
            return False
    return True

# Function backtracing_solver => Generates the solution list.
# Parameters:
# p => partial solution 
# n => dimension of the chessboard
# Ans => flag to determine whether solution is possible or not
def backtracking_solver(p, n, Ans=False):
    if(len(p)==n):
        return p
     
    for i in range(n):
        if i not in p:
            p.append(i)
            
            if(backtracking_checker(p)):
                Ans=backtracking_solver(p,n)
                if(Ans):
                    return Ans

            p.pop()
    return Ans

if __name__ == '__main__':
    print("Enter N: ", end='')
    S=int(input())
    print(backtracking_solver([],S)) 