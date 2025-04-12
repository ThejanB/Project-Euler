
units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'] #10 numbers
teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'] #10 numbers
tens_10x = ['', '','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'] #9 numbers
hundred = 'Hundred'
thousand = 'Thousand'
million = 'Million'
billion = 'Billion'


def get_sentence(number):
    if number == 0:
        return ''
    elif number < 10:
        return units[number]
    elif number < 20:
        return teens[number-10]
    elif number < 100:
        return tens_10x[number//10] + get_sentence(number%10)
    elif number < 1000:
        return units[number//100] + hundred + get_sentence(number%100)
    elif number < 1000000:
        return get_sentence(number//1000) + thousand + get_sentence(number%1000)
    elif number < 1000000000:
        return get_sentence(number//1000000) + million + get_sentence(number%1000000)
    else:
        return get_sentence(number//1000000000) + billion + get_sentence(number%1000000000)


number = int(input())

if number == 0:
    print('Zero')
else:
    sentence = get_sentence(number)
    # add space after each word, after each capital letter
    sentence = ' '.join(''.join(' ' + char if char.isupper() else char for char in sentence).split())
    sentence = sentence.strip()
    print(sentence)
