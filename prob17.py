"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when
writing out numbers is in compliance with British usage.
"""



def num2words(num):
    digit = [0,3,3,5,4,4,3,5,5,4] # zero, one, two, three, four, five, six, seven, eight, nine,
    ten = [3,6,6,8,8,7,7,9,8,8] # ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
    ty = [0,ten,6,6,5,5,5,7,6,6]
    hundred = [ret for ret in map(lambda x: x + 7, digit)] # hundred and
    count = 0
    words = [int(x) for x in str(num)]
    if len(words) == 3: #hundred
        if words[1] == 0 and words[2] == 0: # 100, 200, ...
            count += hundred[words[0]]
        else:
            count += hundred[words[0]] + 3 + ty[words[1]] + digit[words[2]]

    elif len(words) == 2:
        pass
    return words, count


num = 115
print(num2words(num))

# twenty = [6] * 10
# twenty = [x + y for x, y in zip(twenty, digit)]
# thirty = [6] * 10
# thirty = [x + y for x, y in zip(thirty, digit)]
# forty = [5] * 10
# forty = [x + y for x, y in zip(forty, digit)]
# fifty = [5] * 10
# fifty = [x + y for x, y in zip(fifty, digit)]
# sixty = [5] * 10
# sixty = [x + y for x, y in zip(sixty, digit)]
# seventy = [7] * 10
# seventy = [x + y for x, y in zip(seventy, digit)]
# eighty = [6] * 10
# eighty = [x + y for x, y in zip(eighty, digit)]
# ninety = [6] * 10
# ninety = [x + y for x, y in zip(ninety, digit)]
#
# num += sum(twenty) + sum(thirty) + sum(forty) + sum(fifty)
# num += sum(sixty) + sum(seventy) + sum(eighty) + sum(ninety)

# one hundred, one hundred and one
# hundred_digit = [10, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# hundred_digit = [x + y for x, y in zip(hundred_digit, digit)]
# num += sum(hundred_digit)
#
# hundred_digit = [13] * 10
# one hundred and ten,
# hundred_10 = [x + y for x, y in zip(hundred_digit, ten)]
# hundred_20 = [x + y for x, y in zip(hundred_digit, twenty)]
# hundred_30 = [x + y for x, y in zip(hundred_digit, thirty)]
# hundred_40 = [x + y for x, y in zip(hundred_digit, forty)]
# hundred_50 = [x + y for x, y in zip(hundred_digit, fifty)]
# hundred_60 = [x + y for x, y in zip(hundred_digit, sixty)]
# hundred_70 = [x + y for x, y in zip(hundred_digit, seventy)]
# hundred_80 = [x + y for x, y in zip(hundred_digit, eighty)]
# hundred_90 = [x + y for x, y in zip(hundred_digit, ninety)]
# num += sum(hundred_10) + sum(hundred_20) + sum(hundred_30) + sum(hundred_40) + sum(hundred_50)
# num += sum(hundred_60) + sum(hundred_70) + sum(hundred_80) + sum(hundred_90)
