# # # # # # factorial in math package
# # # # # from math import factorial
# # # # # fact = factorial(5)
# # # # # print(fact)

# # # # # # use recursive function when solving factorial
# # # # # def factorial(n):
# # # # #     if n == 1:
# # # # #         return 1
# # # # #     return n * factorial(n-1)

# # # # # print(factorial(6))

# # # # # 재귀함수로 그림을 그리는 프로그램

# # # # # import turtle as t 

# # # # # def spiral(sp_len):
# # # # #     if sp_len <= 5:
# # # # #         return
# # # # #     t.forward(sp_len)
# # # # #     t.right(90)
# # # # #     spiral(sp_len - 5)

# # # # # t.speed(0)
# # # # # spiral(200)
# # # # # t.hideturtle()
# # # # # t.done()

# # # # # 시에르핀스키의 삼각형을 그리는 프로그램
# # # # import turtle as t 

# # # # def tri(tri_len):
# # # #     if tri_len <= 10:
# # # #         for i in range(0, 3):
# # # #             t.forward(tri_len)
# # # #             t.left(120)
# # # #         return
# # # #     new_len = tri_len / 2
# # # #     tri(new_len)
# # # #     t.forward(new_len)
# # # #     tri(new_len)
# # # #     t.backward(new_len)
# # # #     t.left(60)
# # # #     t.forward(new_len)
# # # #     t.right(60)
# # # #     tri(new_len)
# # # #     t.left(60)
# # # #     t.backward(new_len)
# # # #     t.right(60)

# # # # t.speed(-1000)
# # # # tri(160)
# # # # t.hideturtle()
# # # # t.done()

# # # # 나무를 그리는 프로그램
# # # import turtle as t 

# # # def tree(br_len):
# # #     if br_len <= 5:
# # #         return
# # #     new_len = br_len * 0.7
# # #     t.forward(br_len)
# # #     t.right(20)
# # #     tree(new_len)
# # #     t.left(40)
# # #     tree(new_len)
# # #     t.right(20)
# # #     t.backward(br_len)

# # # t.speed(-1000)
# # # t.left(90)
# # # tree(70)
# # # t.hideturtle()
# # # t.done()

# # # 눈꽃을 그리는 프로그램
# # import turtle as t 

# # def snow_line(snow_len):
# #     if snow_len <= 10:
# #         t.forward(snow_len)
# #         return
# #     new_len = snow_len / 3
# #     snow_line(new_len)
# #     t.left(60)
# #     snow_line(new_len)
# #     t.right(120)
# #     snow_line(new_len)
# #     t.left(60)
# #     snow_line(new_len)

# # t.speed(-1000)
# # snow_line(150)
# # t.right(120)
# # snow_line(150)
# # t.right(120)
# # snow_line(150)
# # t.hideturtle()
# # t.done()


# from math import sin,cos,exp,log

# functions = {'sine':sin,
#             'cosine': cos,
#             'exponential': exp,
#             'logarithm': log}

# print(functions)
# print(functions['exponential'])
# print(functions.keys())
# print(functions.values())

# for name in functions:
#     print('The result of {} (1) is {}'.format(name, functions[name](1.0)))
     
def test_sequence(N):
    limit = 1.0
    partial_sum = 1.0

    for n in range(1 , N+1):
        partial_sum = partial_sum + limit
        limit = limit / 2.0
    return limit, partial_sum

if __name__ == '__main__':
    print(test_sequence(50))

