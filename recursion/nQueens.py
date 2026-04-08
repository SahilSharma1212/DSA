# N queens

n = 4
ans = []
'''
FORMAT = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
'''

arr = [0,1,2,3]

def checkValid(currArr):
    st = set()
    for s in currArr:
        st.insert(s.find("Q"))
    
    return len(st) == n

def nQueens(occupiedColList, currIndex, currArr):
    if currIndex == n:
        if checkValid(currArr):
            ans.append(currArr[:])
            return
        else:
            return
    for i in range(n):
        if i not in occupiedColList:
            occupiedColList.append(i)
            currArr.append("."*i + "Q" + "."*(n-i-1))
            nQueens(occupiedColList, currIndex+1, currArr)
            occupiedColList.pop()
            currArr.pop()
