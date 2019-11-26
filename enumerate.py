#how to print both list values and indices

data = ['red','green','blue','white']
 
#lets use a built in function "enumerate"
for index,value in enumerate(data):
  print( '{} {}'.format(index,value))
