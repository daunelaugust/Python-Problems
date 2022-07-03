def pig_it(text):
    # I will optimize soon for "?" and "!" I just got lazy and wanted it to work for sure 
    #? and ! functionatlity
    b = 0
     #Split the string into a list of words
    if text.endswith("?"):
        b = 1
        words = text.split(" ")
        words = words[:-1]
    elif text.endswith("!"):
        b = 2
        words = text.split(" ")
        words = words[:-1]
    else:
        words = text.split(" ")
    
    newlist = [];
    a=0;
    res = "";
   #Making firstletter+ay words
    firstletters = [l[0] for l in words]
    ayletters = [n +"ay" for n in firstletters]
    
    #adding firstletter+ay to words
    for letters in words:
        L = letters+ayletters[a]
        newlist.append(L)
        a+=1

    #making no first letters
    for a in newlist:
        res += a[1:len(a)]+ " "
    if b == 1:
        return res + "?"
    elif b == 2:
        return res + "!"

    return res.strip()