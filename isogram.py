iso=list(input())
yup=[]
for i in iso:
    if i not in yup:
        yup.append(i)
if iso==yup:
   print("Yes")
else:
   print("No")
