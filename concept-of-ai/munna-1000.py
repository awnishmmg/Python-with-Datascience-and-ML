def main():
    inputList = ['1', '99', '256', '512', '1000', '9898', '19', '980', '4550', '55']
    outputList = []

    list2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    numeric_words = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                     'seventeen', 'eighteen', 'nineteen']
    list10 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    for num in inputList:
        numeric = eval(num)
        digits = [eval(x) for x in num]

        print(digits)

        finalStr = ""

        if len(digits) == 3:
            num1 = digits[0]
            num2 = digits[1]
            num3 = digits[2]

            finalStr = list10[num1] + " hundred "

            if 10 < numeric % 100 < 20:
                finalStr += numeric_words[numeric % 10 - 1]
            else:
                if num2 >= 2:
                    str1 = list2[num2 - 2]
                    if num3 == 0:
                        finalStr += str1
                    else:
                        str2 = list10[num3]
                        finalStr += str1 + " " + str2
                elif num2 == 1:
                    finalStr += numeric_words[num3 - 1]
                elif num2 == 0:
                    if num3 != 0:
                        finalStr += list10[num3]

            outputList.append(finalStr.strip())

        elif len(digits) == 2:
            num1 = digits[0]
            num2 = digits[1]

            if 10 < numeric < 20:
                finalStr += numeric_words[numeric % 10 - 1]
            else:
                if num1 >= 2:
                    str1 = list2[num1 - 2]
                    if num2 == 0:
                        finalStr += str1
                    else:
                        str2 = list10[num2]
                        finalStr += str1 + " " + str2
                elif num1 == 1:
                    finalStr += numeric_words[num2 - 1]

            outputList.append(finalStr.strip())

        else: 
            num1 = digits[0]
            finalStr += list10[num1]
            outputList.append(finalStr.strip())
    print(outputList)


main()
