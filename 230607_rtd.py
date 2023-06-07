i=input("주민등록번호를 입력해 주세요 : ")
i1=[]
a=0
a+=int(i[0])*2+int(i[1])*2+int(i[2])*2+int(i[3])*2+int(i[4])*2+int(i[5])*2+str(i1[0])   
+int(i[6])*2+int(i[7])*2+int(i[8])*2+int(i[9])*2+int(i[2])*2+int(i[3])*2+int(i[4])*2+int(i[5])



result=11-(a%11)%10
if result==i[5]:
    print("유효한 주민등록번호 입니다.")
    
else:
    print("유효하지 않은 주민등록번호 입니다.")
