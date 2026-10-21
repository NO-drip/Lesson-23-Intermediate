Country = {'India':'0091', 'Nepal':'0321','Australia':'9831'}

print("Country code for Australia:")
print (Country['Australia'] )

print("Country code for Nepal:")
print(Country['Nepal'])

print("Country code for UAE is:")
print(Country.get('UAE','Not found in dictionary'))