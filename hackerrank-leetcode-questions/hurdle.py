

def highest_hurdle(a, height):
    greatest = 0
    great = a[0]

    for i in range(1, len(a)):
      if a[i] > great:
          great = a[i]

    # return great

    if height > great:
        return 0
    else:
        return(great - height)

a = [1,2,3,4]
height = 3
print(highest_hurdle(a,height))
