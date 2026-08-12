#convert given list into set and print how many unique languages divya knows
#["python","c++","java","python","c","java"]
languageList = ["python","java","c++","python","java","c"]

#convert into set
languageSet = set(languageList)
print(type(languageSet))
print("Divya knows", len(languageSet) , "languages")
