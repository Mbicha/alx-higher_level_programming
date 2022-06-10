def roman_to_int(roman_string):
    roman_num = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900, 'M':1000}
    j = 0
    number = 0
    
    if (type(roman_string) != str) or (roman_string is None):
        return 0
    else:
        len_string = len(roman_string)
        while j < len_string:
            if j + 1 < len_string and roman_string[j:j+2] in roman_num:
                number += roman_num[roman_string[j:j+2]]
                j += 2
            else:
                number += roman_num[roman_string[j]]
                j += 1
        return number
