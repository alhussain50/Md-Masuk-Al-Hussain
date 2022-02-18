#58A

s = str(input())

length_of_s = len(s)

letters_of_s = []

count = 0

for x in s:
    letters_of_s.append(x) 


if s.count('l') > 1:

    for i in range(length_of_s):
        if letters_of_s[i] == 'h':
            key = i
            count = count + 1
            break

    if count == 0:
        print("NO")

    else:
        for i in range(key + 1, length_of_s):
            if letters_of_s[i] == 'e':
                key = i
                count = count + 1
                break

        if count == 1:
            print("NO")

        else:
            for i in range(key + 1, length_of_s):
                if letters_of_s[i] == 'l':
                    key = i
                    count = count + 1
                    break
            
            if count == 2:
                print("NO")

            else:
                for i in range(key + 1, length_of_s):
                    if letters_of_s[i] == 'l':
                        key = i
                        count = count + 1
                        break

                if count == 3:
                    print("NO")
            
            
                else:
                    if key + 1 > length_of_s:
                        print("NO")

                    else:    
                        for i in range(key + 1, length_of_s):
                            if letters_of_s[i] == 'o':
                                key = i
                                count = count + 1
                                break

                    if count == 4:
                        print("NO")
                    elif count == 5:
                        print("YES")

else:
    print("NO")

