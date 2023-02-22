# def inorder(N):
#     if N < len(lst):
#         inorder(N * 2)
#         print(N)
#         inorder(N * 2 + 1)
#
# def inorder(rootidx):
#     if rootidx < len(lst):
#         inorder(rootidx*2)
#         print(rootidx)
#         inorder(rootidx*2+1)



def inorder(rootidx):
    global value
    if rootidx <= N:
        inorder(rootidx*2)
        # print(rootidx)
        lst[rootidx] = value
        value += 1

        # print(value)
        inorder(rootidx*2+1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst= [0] * (N+1)
    value = 1
    ans = inorder(1)
    print(lst)
    print(f'#{tc}', lst[1], lst[N//2])


# def inorder(rootidx):
#     if rootidx <= len(lst):
#         print(rootidx)
#         inorder(rootidx*2)
#         #값채우기
#         inorder(rootidx*2+1)
#
# N = 6
# lst= [0] * N
# print(inorder(1))
