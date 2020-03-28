
n = 10

for s in range(1,n) :
    
    n *= s
    
print('循环',n)

def fu1(ni) :
    '''
    求任意一个数的递归
    '''
    #'''基线条件'''
    if ni == 1 :
        return 1
   # '''递归条件'''
    return ni * fu1(ni-1)
    
        
    
print(fu1(10))
help(fu1)
