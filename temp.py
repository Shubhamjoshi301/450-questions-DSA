s = "{'a':{'c':3,'d':4},'b':2}"
t = "a.c"
d = eval(s)
print(d)
print(type(d))
l = t.split('.')
temp = "d"
for i in l:
    temp+="['"+i+"']"
print(temp)
print(eval(temp))