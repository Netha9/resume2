   x = 121
   l = len(str(x))
   value = 0
        while(l>0):
            rem = x%10**l-1
            value = value + rem*10**l-1
            l = l-1
            x = x//10**l-1
        return value == x