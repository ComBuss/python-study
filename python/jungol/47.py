close_price_daeshin = [10000,10500,10300,10700,11100]

average = 0
for i in close_price_daeshin:
    i = int(i)
    average += i

print('average: %s' % (average/5))
