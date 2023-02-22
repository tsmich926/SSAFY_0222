def inorder(root):
    global ans
    if root:
        inorder(int(TREE[root][1]))
        ans += (TREE[root][0])
        inorder(int(TREE[root][2]))


for tc in range(1,11):
    N = int(input())
    TREE = [[0]*3 for _ in range(N+1)] #배열안에 정보 저장하려고 만듬
    ans = " "
    for _ in range(N):
        lst = input().split() #입력받기
        node = int(lst[0]) #노드의 숫자가 됨
        TREE[node][0:len(lst)-1] = lst[1:]

    # print(TREE)
    inorder(1)

    print(f'#{tc} {ans}')