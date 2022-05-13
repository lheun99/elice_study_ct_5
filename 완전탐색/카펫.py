def solution(brown, yellow):
    yellows = []
    # yellow 약수 구하기
    # yellow 개수로 가능한 격자 모양들 확인
    for y_height in range(1, yellow + 1):
        if (yellow % y_height == 0):
            if (y_height <= yellow//y_height):
                yellows.append([y_height, yellow//y_height])

    # yellow모양에 따른 brown개수 확인
    for b_height, b_width in yellows:
        b = (b_height*2) + (b_width+2)*2
        if(b == brown):
            return ([b_width+2, b_height+2])


print(solution(8, 1))

# 약수 구하기 다른 방법
# https://minnit-develop.tistory.com/16
# for i in range(1, int(n**(1/2)) + 1):
#         if (n % i == 0):
#             divisorsList.append(i)
#             if ((i**2) != n):
#                 divisorsList.append(n // i)

#     divisorsList.sort()
