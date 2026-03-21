num = 11
not_found = True


while not_found:
    not_found = False
    value = sorted(str(num))
    for i in range(2, 7):
        if sorted(str(i * num)) != value:
            not_found = True
            break
    
    if not not_found:
        print(num)

    num += 1