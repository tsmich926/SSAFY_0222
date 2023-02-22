def preorder(root):
    global cnt
    if root:
        preorder(leftc[root])
        cnt += 1
        preorder(rightc[root])
    return cnt



T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split()) #간선갯수 ,주어진 노드를 루트로
    lst = list(map(int,input().split()))

    leftc = [0] * (E + 2) #간선의 갯수+1이 노드의 갯수이므로
    rightc = [0] * (E + 2)
    cnt = 0

    for idx in range(0, len(lst), 2):
        p = lst[idx]
        c = lst[idx + 1]

        if leftc[p] == 0:  # 비었다
            leftc[p] = c
        else:
            rightc[p] = c

    print(leftc)
    print(rightc)

    ans = preorder(N)

    print(f'#{tc} {ans}')

