#wap in python to show all the possible no of keywords:-
#python : 35 Keyword : Hard keywords 
#python : 4 Keyword : soft keywords

#Keyword : 35 True,False,None :=> capital => lower case 
# keywords : are reserved words that perform special task 
# keyword : are part langauge fundamental

import keyword
keywords = keyword.kwlist

count = 0
print('No of keywords (Hard):',len(keywords))
for kw in keywords:
    if count == 4:
       print() #new line
       count = 0
    else:
        print("\t",kw,end="")
        count = count + 1
    
print('soft keywords:',keyword.softkwlist)
print('No of softkeywords:',len(keyword.softkwlist))