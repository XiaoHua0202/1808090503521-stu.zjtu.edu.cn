def fu1(s) :
    '''这是一个回文检查'''
    
    if len(s) < 2 : # 基线条件
        return True
    elif s[0] != s[-1] :
        return False
    # 递归条件
    return fu1(s[1:-1] )
print(fu1('12321'))
