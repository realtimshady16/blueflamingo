#Job Counter

f = open("jobs.txt", "r")
list = f.readlines()

def makeSet():
    mySet = set()
    for i in range(6, 12):
        set.add(list[i])
    return mySet

def main():
    mySet = makeSet()
    