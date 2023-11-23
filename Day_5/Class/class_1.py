
# tup = (i for i in range(10))
# a= tuple(tup)
# print(a)

# # dung thuat ngu packing de chuyen sang tuple
# tup_1 = 1, 2,3 


n = int(input())
s = list(map(int, input().split()))
N = int(input())

s.reverse()
s = set(s)
for _ in range(N):
    command = input().split()
    if len(command) > 1:
        com = f"s.{command[0]}({command[1]})"
        eval(com)
    else:
        com = f"s.{command[0]}()"
        eval(com)
            
print(sum(s))


# n = int(input())
# s = list(map(int, input().split()))
# N = int(input())
# s = set(s)
# s.pop()
# s.remove(9)
# s.discard(9)
# s.discard(8)
# s.remove(7)
# s.pop()
# s.discard(6)
# s.remove(5)
# s.pop()
# s.discard(5)

# print(s)