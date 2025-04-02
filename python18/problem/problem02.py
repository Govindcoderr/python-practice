def hand_shack(n):

    return (n * (n-1))//2


n = 10
print("total hand-shack:" ,hand_shack(n))

#  one more way to slove this problem
# 

def handshake(n):
    count=0

    for i in range(n):
        count +=i 
        
    
    return count

n=10
print("total hand-shake:", handshake(n))


