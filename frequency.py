Dictionary = {'Apple':2,'Orange':2,'Banana':2,'Papaya':1,'WaterMelon':2}
print ("The values in Dictionary are:",(str(Dictionary)))
Result = 0
for i in Dictionary:
    if Dictionary[i] == 2:
        Result += 1

print("The frequency of two in Dictionary is:",(str(Result)))

