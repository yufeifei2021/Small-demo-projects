s = (('chen_yu', 'F', 2), ('chen_yu', 'M', 3), ('jing_yi', 'F', 2), ('jing_yi', 'M', 1))

new = []
for i in range(len(s)):
    # 第一个
    if i == 0:
        if s[i][0] == s[i+1][0]:
            max_2 = lambda x, y: x if x[2] > y[2] else y
            new.append(max_2(s[i], s[i+1]))
        else:
            new.append(s[i])
    # 最后一个
    elif i == len(s)-1:
        if s[i][0] == s[i-1][0]:
            pass
        else:
            new.append(s[i])
    elif s[i][0] == s[i+1][0]:
        max_2 = lambda x, y: x if x[2] > y[2] else y
        new.append(max_2(s[i], s[i+1]))
        
print(new)