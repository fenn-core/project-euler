num_str = ""

num = 1
flag = True
while 1_000_000 >= len(num_str):
    num_str += str(num)
    num += 1 
    
val = (int(num_str[0]) * int(num_str[9]) * int(num_str[99]) * int(num_str[999])
          * int(num_str[9_999]) * int(num_str[99_999]) * int(num_str[999_999])) 

print(val)