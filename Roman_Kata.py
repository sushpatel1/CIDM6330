class NumeralsToRoman:
   

   def __init__(self, number) -> None:
       self.number = number

   def __str__(self) -> str:
        roman = NumToRoman()
        return f"{roman}"

    
def NumToRoman(self):
       Number = self.number
       dict = { 1000:"M", 900:"CM", 500:"D", 400:"CD",
                100:"C", 90:"XC", 50:"L", 40:"XL",
                10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I" }

       roman_number = ''
       i = 0
       while  Number > 0:
           for k, v in dict.items():
            while Number >= k:
                roman_number += v
                Number -= k

           # for a in range(Number // val[i]):
            #    roman_number += syb[i]
            #    Number -= val[i]
           # i += 1
       return roman_number







            






