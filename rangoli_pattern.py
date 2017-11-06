number = int(input())
if (number<=26):
    last_char = ord('a') + number - 1
    list_ = []
    for i in range(0,number):
        list_.append(chr(last_char))
        sorted_list = sorted(list_)
        print(('-'.join(list_)).rjust(2*number - 1 , '-') + (('-'.join(sorted_list))[1:]).ljust(2*number - 2 , '-'))
        last_char = last_char - 1

    for i in range(0,number-1):
        list_.pop()
        sorted_list = sorted(list_)
        print(('-'.join(list_)).rjust(2*number - 1 , '-') + (('-'.join(sorted_list))[1:]).ljust(2*number - 2 , '-'))

else:
    print(("Try Again..!!").center(50,'-'))
    print(("Enter a number between 1 and 26").center(50,'-'))
