# forkNum(n) return total process( including itself) after n fork operation in a row:
# ex : forkNum(3) is like
#    main() {
#      fork()
#      fork()
#      fork()
#    }
# this is inspired by https://www.geeksforgeeks.org/operating-systems-set-5/ question1
def forkNum(n):
    childrenNum = 0
    for i in range(n):
        childrenNum += forkNum(i)
    return childrenNum + 1 # + 1 is to take care of it self

def main():
    for i in range(5):
        print("forkNum(%d): %d\n"%(i, forkNum(i)))

if __name__ == "__main__":
    main()