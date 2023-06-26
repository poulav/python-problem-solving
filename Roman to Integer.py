class Solution:
    def romanToInt(self, s: str) -> int:        
        romanNumberSystem = ['I', 'V', 'X', 'L', 'C', 'D', 'M',]
        romanToInteger = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        sumOfNumbers = 0
        lengthOfString = len(s)
        counter = 0
        for currentCharacter in s:
            if((counter+1)<(lengthOfString)):
                nextCharacter = s[counter+1]
            else:
                nextCharacter = '' 
            lastCounter = counter-1
            if(lengthOfString>1):
                if(nextCharacter!='' and (romanNumberSystem.index(nextCharacter)>romanNumberSystem.index(currentCharacter))):
                    sumOfNumbers = sumOfNumbers + (romanToInteger[nextCharacter] - romanToInteger[currentCharacter])
                elif((lastCounter>-1) and (romanNumberSystem.index(s[counter-1])<romanNumberSystem.index(currentCharacter))): 
                    counter+=1                   
                    continue
                else:
                    sumOfNumbers = sumOfNumbers + romanToInteger[currentCharacter]
                counter+=1
            else:
                sumOfNumbers = sumOfNumbers + romanToInteger[currentCharacter]
        return sumOfNumbers
    
s = "D"
objSolution = Solution()
ret = objSolution.romanToInt(s)
print(ret)
