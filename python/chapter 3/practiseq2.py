#write aprogram to take your fav food as input and print middle 3 characters and last 2 characters
food = input("Enter  yuor fav food: ")
mid = len(food)//2
first3 = print(food[mid-1:mid+2])
last2 = print(food[-2:])