input_string = input()
array=[]
array = input_string.split(" ")
def comparision(arr):
  n=int(arr[0])
  n1=int(arr[1])
  n2=int(arr[2])
  n3=int(arr[3])
  print(n,n1,n2,n3)
  a = abs(n-n1) 
  b = abs(n-n2)  
  c = abs(n-n3) 
  d = min(a,b,c)
  # 
  arr1 = [a,b,c]
  y = arr1.index(d)+1
  print(arr[y])
 
      


     

comparision(array)