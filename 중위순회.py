T = int(input())
for tc in range(1,T+1):
    N = int(input())
    value = ['-'] *(N+1)
    rightc = [0] *(N + 1)
    leftc = [0] * (N + 1)
    lst = []


    for i in range(N):
        lst = list(input().split())
        # st2.a
        # ppend(lst[1:])
        print(lst)
        idx = int(lst[0])
        value[idx] = lst[1]
        if len(lst)==3:
            leftc[idx] = lst[2]
            rightc[idx] = lst[3]
        if len(lst)==2:
            rightc[idx] = lst[3]
        print(lst)


    # # 리스트의 길이가 3이면 우좌 자식 존재
    # # 길이가 2이면 우 자식 존재
    # # 길이가 1이면 자식 없음
    # for i in range(len(lst)):
    #     if len(lst2[i]) == 3:
    #         rightc[i] = lst[i][1]
    #         leftc[i] = lst[i][2]
    #     elif len(lst2[i]) == 2:
    #         rightc[i] = lst[i][1]