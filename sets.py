def isSubset(L1, L2):
    matched = False
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        matched = False
    return matched



def getBinStr(n, length):    
    result = ''
    while n>0:
        result = str(n%2) + result
        n = n/2

    if len(result) > length:
        raise ValueError("Not enough digits")    

    while len(result) < length:
        result = '0'+result
    print "bin string: {}".format(result)
    return result
    
    
def powerSet(L):    
    ps = []
    for i in range(2**len(L)):
        binStr = getBinStr(i, len(L))
        subset=[]
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
                
        ps.append(subset)
    return ps[:]
            
            

ps = powerSet(['a', 'b', 'c', 'd'])
#ps = powerSet(['a'])
print "size of power set {}".format(len(ps))
print "power set {}".format(ps)
