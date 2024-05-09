# # # def find_divisors(n):
# # #     divisors = set()
# # #     for i in range(1, int(n**0.5) + 1):
# # #         if n % i == 0:
# # #             divisors.add(i)
# # #             divisors.add(n // i)
# # #     return divisors

# # # def gcd_using_sets(a, b):
# # #     # 두 수의 약수를 집합으로 구함
# # #     divisors_a = find_divisors(a)
# # #     divisors_b = find_divisors(b)

# # #     # 두 집합의 교집합을 구함
# # #     common_divisors = divisors_a.intersection(divisors_b)

# # #     # 교집합에서 가장 큰 수를 반환
# # #     return max(common_divisors)

# # # # 예시로 36과 60의 최대 공약수를 구해보기
# # # result = gcd_using_sets(36, 60)
# # # print(f"The GCD of 36 and 60 is {result}")

# # f = open("123.txt", "r")
# # a = f.read().split(" ")
# # set(a)
# # print(len(a), a)

# try:
#     pass
# except ZeroDivisionError as e:
#     print(e)

# except ValueError as e:
#     print (e)

# except Exception as e:
#     print(e)

# finally:
#     pass

# 프로그램이 오류가 났을 경우 근본적인 문제를 찾아 해결하기 위하여
