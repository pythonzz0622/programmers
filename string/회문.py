string = 'level3'

left = 0 
right = len(string) - 1

is_palindrom  = True
while left < right:
    if string[left] == string[right]:
        left += 1
        right -= 1
        continue
    else:
        is_palindrom = False
        break

print(is_palindrom)
        