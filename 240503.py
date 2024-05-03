# # # # # # # s = {1, 2, 3}
# # # # # # # s.add(5)
# # # # # # # print(s)

# # # # # # # s.update([4, 5, 6])
# # # # # # # print(s)

# # # # # # # s.remove(3)
# # # # # # # print(s)

# # # # # # # s.discard(6)
# # # # # # # print(s)


# # # # # # def count_unique_words(text):
# # # # # #     words=text.split()

# # # # # #     unique_words

# # # # # f = open("C:\Users\gusal\Desktop\test.txt", "w")
# # # # # print(f.read())
# # # # # f.close()

# # # # # f.open('test.txt')
# # # # # print(f.read(11))
# # # # # print(f.readline())
# # # # # f.close()

# # # # # f.open('test.txt')
# # # # # print(f.readlines())
# # # # # f.close()

# # # # from tkinter import *
# # # # from tkinter.filedialog import *

# # # # readFile = askopenfilename()
# # # # if readFile != None:
# # # #     infile = open(readFile, "r")

# # # # s = infile.read()
# # # # print(s)
# # # # infile.close()

# # # (x, y) = (2, 0)
# # # try:
# # #     z = x / y
# # # except ZeroDivisionError:
# # #     print("0으로 나누는 예외")

# # while True:
# #     try:
# #         n = input("정수입력 : ")
# #         n = int(n)
# #         break
# #     except ValueError as e:
# #         print("정수 입력 오류 : ", e)
# # print("정수입력성공")

# try:
#     f = open("test2.txt", "r")
#     print(f.read())
# except IOError:
#     print("파일 입출력 오류 발생")
# finally:
#     f.close()
#     print("finally 블록 수행")

while True:
    try:
        a = int(input("나눠지는 수를 입력하세요 : "))
        b = int(input("나누는 수를 입력하세요 : "))
        result = a / b
    except ValueError as e:
        print("정수를 입력해야합니다")
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print("오류가 발생했습니다.")
    else:
        print("나누기 연산 성공")
        print("결과 : ", result)
    finally:
        print("프로그램을 종료합니다")
