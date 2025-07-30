
import sys

MIN_RANGE = 0
MAX_RANGE = 10

def munna(num):
    print ("hello jii !  mai munna ")
    tens=['ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','hundred']
    ones=['one','two','three','four','five','six','seven','eight','nine']
    elevenmore=['eleven ','twelve','thirteen','fourteen','fifteen','sisteen','seventeen','eighteen','nineteen']

    if num>20:
        r = num%10
        q = int (num)/10
        if r != 0:

            print("r : ",r, "q : ",int(q))
            first=tens[int(q)-1]
            second=ones[r-1]
            print(first +"-", second)
        else:
            print(tens[int(q)-1])

    elif num ==10 :
            print("ten")

    elif num<10:
        print(ones[num-1])
    elif num>10 and  num < 20 :
        r = num%10
        q = int (num)/10
        print(elevenmore[r-1])
    
        
def main():
    no = eval(input('Enter the no:'))
    munna(no)
    
    
def getAnalytics():
    scores = {
           'confidence_score':1,
           'min_range':MIN_RANGE,
           'max_range':MAX_RANGE,
           'accuracy':getAccuracy(MIN_RANGE,MAX_RANGE)
    }
    print(scores)
    
def getAccuracy(MIN_RANGE,MAX_RANGE):

    import random as rd
    inputs = [rd.randint(MIN_RANGE,MAX_RANGE) for no in range(MIN_RANGE,MAX_RANGE+1)]
    
    print(index)
    print(inputs)
    
    
sys.exit(getAccuracy(MIN_RANGE,MAX_RANGE))

