#705A

n = int(input())

string_1 = 'I hate '
string_2 = 'that I love '
string_3 = 'that I hate '
string_4 = 'it'
final_string = 'I hate '


for i in range(1, n):
    if i % 2 != 0:
        final_string = final_string + string_2
    else:
        final_string = final_string + string_3

final_string = final_string + string_4
print(final_string)

    
