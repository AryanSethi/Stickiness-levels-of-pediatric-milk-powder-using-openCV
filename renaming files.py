import os

path= "D:/work/Milk Project/turbidity difference/Light_behind/shades/"
i=1

for filename in os.listdir(path):
      my_dest =str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      os.rename(my_source, my_dest)
      i =i+1
