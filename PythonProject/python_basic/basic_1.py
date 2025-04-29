b,c,d=10,20,30
print(f"b={b},c={c},d={d}")

# sql = f"select*from emp where empno={empno}"
# 같은 값을 가지고 있는 경우 => 주소값이 동일
a1 = 3
b1 = 3
print(id(a1),id(b1))

m=10
n=20
print(f"m={m}",end=" ") # print
print(f"n={n}") # println
print("m:%d" %m, "n:%d" %n , sep="-")
# 구분자 sep
# 출력물 / end / sep