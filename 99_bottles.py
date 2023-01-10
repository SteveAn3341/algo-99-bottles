def bottle_song():
	# write your code here!
	number_of_bottles=99
	while(number_of_bottles>2):
		print(f"{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer. Take one down and pass it around, {number_of_bottles - 1} bottles of beer on the wall.")
		number_of_bottles-=1
	print("2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.")
	print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
bottle_song()
