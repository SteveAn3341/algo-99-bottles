str = ""
for i in range(99, 2, -1):
    str += (f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} bottles of beer on the wall.\n")  
    
str_left = "2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall. 1 bottle of beer on the wall,1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.\n"
    

print(str + str_left)




	



