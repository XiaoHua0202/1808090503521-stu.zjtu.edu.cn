def fu (n,i) :
    '''这是求任意数的幂运算'''

# 基线条件    
    if i == 0 :
        return 1
# 递归运算

    return n * fu(n,i-1)
print(fu(2,8))
