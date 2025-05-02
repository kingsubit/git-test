students = [('안뇽', 84), ('인덕', 71), ('인컴', 96), ('박상준', 14)]
max_score=-1
top_student=""
for name, score in students:
     if score > max_score:
         max_score = score
         top_student = name
print("최고 점수 학생 :",top_student,max_score)


fruits=input("단어를 입력하시오:").split()
result={}
for fruit in fruits:
     if fruit in result:
          result[fruit] += 1
     else:
          result[fruit]=1
print(result)