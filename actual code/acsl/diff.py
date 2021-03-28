def diff(str1, str2):
    list_for_strings1 = []
    list_for_strings2 = []
    list_for_strings3 = []
    list_for_strings4 = []

    dupe1 = str1
    dupe2 = str2

    reverse1 = str1[::-1]
    reverse2 = str2[::-1]

    duper1 = str1[::-1]
    duper2 = str2[::-1]

###########################################################

    for i in dupe1:
        if i in dupe2:
            list_for_strings1.append(dupe2[dupe2.index(i)])
            dupe2 = dupe2[dupe2.index(i) + 1 : ]
    
    for i in str2:
        if i in str1:
            list_for_strings2.append(str1[str1.index(i)])
            str1 = str1[str1.index(i) + 1 : ]

    for i in duper2:
        if i in duper1:
            list_for_strings3.append(duper1[duper1.index(i)])
            duper1 = duper1[duper1.index(i) + 1 : ]

    for i in reverse1:
        if i in reverse2:
            list_for_strings4.append(reverse2[reverse2.index(i)])
            reverse2 = reverse2[reverse2.index(i) + 1 : ]

##########################################################

    common = []
    for i in list_for_strings1:
        if i in list_for_strings2 and i in list_for_strings3 and i in list_for_strings4:
            common.append(i)

    common = list(set(common))
    common.sort()

    return common
    
# print(diff('abcddef', 'vdfaddwf'))
# print(diff('friends', 'afraid'))
# print(diff('delicious', 'indiginous'))
# print(diff('happy', 'shipshape'))