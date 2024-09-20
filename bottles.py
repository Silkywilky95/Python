bottles = 99

while bottles > 0: 
    if bottles > 1: 
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        if bottles == 1: 
            print(f"Take one down and pass it around, {bottles} bottle of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")

    else:
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        bottles -= 1
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")



print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
