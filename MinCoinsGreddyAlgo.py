# Returns the minimum number of coins to get the required denominations.
def MinCoins(T,N):
  count = 0
  y = sorted(T, reverse=True)
  for val in y:
    while N >= val:
          N -= val
          count += 1
  if N == 0:
    return("The required minimum number of coins to get the denomination: " + str(count))
  else:
    return("The required denomination cannot be obtained using coins of following quantity. ")

x = MinCoins([20,30,40],130)  
print(x)
