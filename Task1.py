print("Введите исходную строку")
alf="ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a=input()
b=""
c=""
for i in range(len(a)):
    k=0
    for j in range(59):
        if a[i]==alf[j]:
            b=b+alf[j+59]
            k=1
    if k==0:
        b=b+a[i]
print(b);
for i in range(len(b)):
    k=0
    for j in range(len(b)):
        if b[i]==b[j]:
            k=k+1
    if k==1:
        c=c+"("
    else:
        c=c+")"
print(c);
