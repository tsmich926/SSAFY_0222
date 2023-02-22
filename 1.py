
# pre(i)
# if i >0
#     print(i)
#     pre(c1[i])
#     pre(c2[i])
#
# 연습문제)

# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# lst = list(map(int,s.split()))
# TR = [[] for _ in range(N+1)]
# for idx in range(0,len(lst),2):
#     p=lst[idx]
#     c=lst[idx+1]
# 
#     TR[p].append(c)
# 
# print(TR)


def preorder(root):
    print(root)
    if len(TR[root]):
        preorder(TR[root][0]) #오른쪽 섭트리
    if len(TR[root]) == 2:
        preorder(TR[root][1]) #왼쪽 섭트리
    print(root)

    N = 13
    s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
    lst = list(map(int,s.split()))
    TR = [[] for _ in range(N+1)]
    for idx in range(0,len(lst),2):
        p=lst[idx]
        c=lst[idx+1]

        TR[p].append(c)

    print(TR)

    def inorder(root):
        if len(TR[root]):
            inorder(TR[root][0])
        if len(TR[root]) == 2 :
            inorder(TR[root][1])
        print(root)

------
# def preorder(root):
#     print(root)
#     if leftc[root]:
#         preorder(leftc[root])
#     if rightc[root]:
#         preorder(rightc[root])

    def preorder(root):
        if root:
            print(root)
            preorder(leftc[root])
            preorder(rightc[root])


    N = 13
    s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
    lst = list(map(int,s.split()))

    leftc=[0]*(N+1)
    rightc=[0]*(N+1)

    for idx in range(0,len(lst),2):
        p = lst[idx]
        c = lst[idx+1]

        if leftc[p] == 0: #비었다
            leftc[p] = c
        else:
            rightc[p] = c
    print(leftc)
    print(rightc)

-------------

leftc = [0] * (N + 1)
rightc = [0] * (N + 1)
parent=  [0] * (N + 1)

#부모를 찾아주는 함수
def findA(c):
    while c!=0:
        p = parent[c]
    print(p)
    c = p


-------
def inorder(rootidx):
    if rootidx < len(lst):
        inorder(rootidx*2)
        print(rootidx)
        inorder(rootidx*2+1)

lst = ['0','A','B','C','D','E','F','G','H','I'] + [0]*100
print(lst)

inorder(1)

def finda(idx):
    while idx//2 >= 1:
        idx = idx//2
        print(lst[idx])

