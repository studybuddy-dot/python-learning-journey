#function that takes a string and returns count of vowel and consonants

def countVowCons(userInput):

    vowels="aeiouAEIOU"
    countVowel=0
    countConsonant=0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel+=1
            else:
                countConsonant+=1

    return countVowel,countConsonant

vowel,consonant=countVowCons("sanyukta joshi") 
print("Vowels=",vowel,"Consonants=",consonant)   