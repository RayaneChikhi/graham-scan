import matplotlib.pyplot as plt

### Functions that were given by the original exam #######

def newStack():
    return []

def isEmpty(s):
    return s==[]

def push(i,s):
    s.append(i)

def top(s):
    return s[-1]

def pop(s):
    a = s[-1]
    s.pop()
    return a

################################################################

## Functions required that weren't mentioned in the exam #######

def sort_lists(A, B):
    C = list(zip(A, B))
    C.sort(key=lambda x: x[0])
    A_sorted, B_sorted = zip(*C)
    
    return [list(A_sorted),list(B_sorted)]



##################################################################



def plusBas(tab, n):
    ans = 0
    for i in range(1, n):
        if tab[1][i] < tab[1][ans] or tab[1][i] == tab[1][ans] and tab[0][i] < tab[0][ans]:
            ans = i
    return ans

def orient(tab, i, j, k):
    a, b = tab[0][j] - tab[0][i], tab[0][k] - tab[0][i]
    c, d = tab[1][j] - tab[1][i], tab[1][k] - tab[1][i]
    det = a * d - b * c
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0


def majES(tab, es, i):
    j = pop(es)
    while not isEmpty(es):
        k = top(es)
        if orient(tab, i, j, k) > 0:
            break
        j = pop(es)
    push(j, es)
    push(i, es)


def majEI(tab, ei, i):
    j = pop(ei)
    while not isEmpty(ei):
        k = top(ei)
        if orient(tab, i, j, k) < 0:
            break
        j = pop(ei)
    push(j, ei)
    push(i, ei)


def convGraham(tab, n):
    ei = newStack()
    es = newStack()
    tab=sort_lists(tab[0],tab[1])
    push(0, ei)
    push(0, es)
    for i in range(1, n):
        majES(tab, es, i)
        majEI(tab, ei, i)
    pop(es)
    while not isEmpty(es):
        push(pop(es), ei)
    
    plt.rcParams["figure.figsize"] = [float(max([tab[0][i] for i in ei])) , float(max([tab[1][i] for i in ei]))]
    plt.rcParams["figure.autolayout"] = True
    plt.grid()
    x_values = [tab[0][i] for i in ei]
    y_values = [tab[1][i] for i in ei]
    plt.plot(x_values, y_values, 'bo', linestyle="--")
    x=[tab[0][i] for i in range(n) if i not in ei]
    y=[tab[1][i] for i in range(n) if i not in ei]
    plt.plot(x, y, 'r*')
    for i in range(n):   
        plt.text(tab[0][i]-0.015, tab[1][i]+0.25, "(" + str(tab[0][i])+','+str(tab[1][i])+")")
    plt.show()

tab = [[0,1,1,4,4,5,5,7,7,8,11,13],[0,4,8,1,4,9,6,-1,2,5,6,1]]
convGraham(tab,12)
#This algorithm runs in O(nlog(n)) 
