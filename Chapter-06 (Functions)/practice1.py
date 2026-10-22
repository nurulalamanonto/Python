#Write a function that returns the counts of vowel & consonant of an user given string input

def countVC(userInput):
    vowels = "aeiouAEIOU"
    countVowels = 0 #Local variable (Can't access outside of this function)
    countCons = 0   #Local variable

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowels += 1
            else:
                countCons += 1
    return countVowels,countCons

Vow,Cons = countVC("Nurul Alam Anonto") #Global variable(Can be accessed any where of the code

print(f"Total Vowels in the string is: {Vow},\nTotal Consonant is the string is: {Cons}")