# # # s = {1, 2, 3}
# # # s.add(5)
# # # print(s)

# # # s.update([4, 5, 6])
# # # print(s)

# # # s.remove(3)
# # # print(s)

# # # s.discard(6)
# # # print(s)


# # def count_unique_words(text):
# #     words=text.split()

# #     unique_words

# f = open("C:\Users\gusal\Desktop\test.txt", "w")
# print(f.read())
# f.close()

# f.open('test.txt')
# print(f.read(11))
# print(f.readline())
# f.close()

# f.open('test.txt')
# print(f.readlines())
# f.close()

from tkinter import *
from tkinter.filedialog import *

readFile = askopenfilename()
if readFile != None:
    infile = open(readFile, "r")

s = infile.read()
print(s)
infile.close()
