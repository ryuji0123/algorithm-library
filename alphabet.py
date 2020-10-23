def num2alpha(num):
    if num <= 26:
        return chr(ord('a') - 1 + num)
    if num % 26 == 0:
        return num2alpha(num // 26 - 1)+chr(ord('z'))
    return num2alpha(num // 26)+chr(ord('a') - 1 + num % 26)
