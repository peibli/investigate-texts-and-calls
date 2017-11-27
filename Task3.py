#-*- coding:utf-8 -*- 
"""
Ã¤Â¸â€¹Ã©ï¿½Â¢Ã§Å¡â€žÃ¦â€“â€¡Ã¤Â»Â¶Ã¥Â°â€ Ã¤Â¼Å¡Ã¤Â»Å½csvÃ¦â€“â€¡Ã¤Â»Â¶Ã¤Â¸Â­Ã¨Â¯Â»Ã¥ï¿½â€“Ã¨Â¯Â»Ã¥ï¿½â€“Ã§Å¸Â­Ã¤Â¿Â¡Ã¤Â¸Å½Ã§â€�ÂµÃ¨Â¯ï¿½Ã¨Â®Â°Ã¥Â½â€¢Ã¯Â¼Å’
Ã¤Â½Â Ã¥Â°â€ Ã¥Å“Â¨Ã¤Â»Â¥Ã¥ï¿½Å½Ã§Å¡â€žÃ¨Â¯Â¾Ã§Â¨â€¹Ã¤Â¸Â­Ã¤Âºâ€ Ã¨Â§Â£Ã¦â€ºÂ´Ã¥Â¤Å¡Ã¦Å“â€°Ã¥â€¦Â³Ã¨Â¯Â»Ã¥ï¿½â€“Ã¦â€“â€¡Ã¤Â»Â¶Ã§Å¡â€žÃ§Å¸Â¥Ã¨Â¯â€ Ã£â‚¬â€š
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
Ã¤Â»Â»Ã¥Å Â¡3:
(080)Ã¦ËœÂ¯Ã§ï¿½Â­Ã¥Å Â Ã§Â½â€”Ã¥Â°â€�Ã§Å¡â€žÃ¥â€ºÂºÃ¥Â®Å¡Ã§â€�ÂµÃ¨Â¯ï¿½Ã¥Å’ÂºÃ¥ï¿½Â·Ã£â‚¬â€š
Ã¥â€ºÂºÃ¥Â®Å¡Ã§â€�ÂµÃ¨Â¯ï¿½Ã¥ï¿½Â·Ã§Â ï¿½Ã¥Å’â€¦Ã¥ï¿½Â«Ã¦â€¹Â¬Ã¥ï¿½Â·Ã¯Â¼Å’
Ã¦â€°â‚¬Ã¤Â»Â¥Ã§ï¿½Â­Ã¥Å Â Ã§Â½â€”Ã¥Â°â€�Ã¥Å“Â°Ã¥Å’ÂºÃ§Å¡â€žÃ§â€�ÂµÃ¨Â¯ï¿½Ã¥ï¿½Â·Ã§Â ï¿½Ã§Å¡â€žÃ¦Â Â¼Ã¥Â¼ï¿½Ã¤Â¸Âº(080)xxxxxxxÃ£â‚¬â€š

Ã§Â¬Â¬Ã¤Â¸â‚¬Ã©Æ’Â¨Ã¥Ë†â€ : Ã¦â€°Â¾Ã¥â€¡ÂºÃ¨Â¢Â«Ã§ï¿½Â­Ã¥Å Â Ã§Â½â€”Ã¥Â°â€�Ã¥Å“Â°Ã¥Å’ÂºÃ§Å¡â€žÃ¥â€ºÂºÃ¥Â®Å¡Ã§â€�ÂµÃ¨Â¯ï¿½Ã¦â€°â‚¬Ã¦â€¹Â¨Ã¦â€°â€œÃ§Å¡â€žÃ¦â€°â‚¬Ã¦Å“â€°Ã§â€�ÂµÃ¨Â¯ï¿½Ã§Å¡â€žÃ¥Å’ÂºÃ¥ï¿½Â·Ã¥â€™Å’Ã§Â§Â»Ã¥Å Â¨Ã¥â€°ï¿½Ã§Â¼â‚¬Ã¯Â¼Ë†Ã¤Â»Â£Ã¥ï¿½Â·Ã¯Â¼â€°Ã£â‚¬â€š
 - Ã¥â€ºÂºÃ¥Â®Å¡Ã§â€�ÂµÃ¨Â¯ï¿½Ã¤Â»Â¥Ã¦â€¹Â¬Ã¥ï¿½Â·Ã¥â€ â€¦Ã§Å¡â€žÃ¥Å’ÂºÃ¥ï¿½Â·Ã¥Â¼â‚¬Ã¥Â§â€¹Ã£â‚¬â€šÃ¥Å’ÂºÃ¥ï¿½Â·Ã§Å¡â€žÃ©â€¢Â¿Ã¥ÂºÂ¦Ã¤Â¸ï¿½Ã¥Â®Å¡Ã¯Â¼Å’Ã¤Â½â€ Ã¦â‚¬Â»Ã¦ËœÂ¯Ã¤Â»Â¥ 0 Ã¦â€°â€œÃ¥Â¤Â´Ã£â‚¬â€š
 - Ã§Â§Â»Ã¥Å Â¨Ã§â€�ÂµÃ¨Â¯ï¿½Ã¦Â²Â¡Ã¦Å“â€°Ã¦â€¹Â¬Ã¥ï¿½Â·Ã¯Â¼Å’Ã¤Â½â€ Ã¦â€¢Â°Ã¥Â­â€”Ã¤Â¸Â­Ã©â€”Â´Ã¦Â·Â»Ã¥Å Â Ã¤Âºâ€ 
   Ã¤Â¸â‚¬Ã¤Â¸ÂªÃ§Â©ÂºÃ¦Â Â¼Ã¯Â¼Å’Ã¤Â»Â¥Ã¥Â¢Å¾Ã¥Å Â Ã¥ï¿½Â¯Ã¨Â¯Â»Ã¦â‚¬Â§Ã£â‚¬â€šÃ¤Â¸â‚¬Ã¤Â¸ÂªÃ§Â§Â»Ã¥Å Â¨Ã§â€�ÂµÃ¨Â¯ï¿½Ã§Å¡â€žÃ§Â§Â»Ã¥Å Â¨Ã¥â€°ï¿½Ã§Â¼â‚¬Ã¦Å’â€¡Ã§Å¡â€žÃ¦ËœÂ¯Ã¤Â»â€“Ã§Å¡â€žÃ¥â€°ï¿½Ã¥â€ºâ€ºÃ¤Â¸Âª
   Ã¦â€¢Â°Ã¥Â­â€”Ã¯Â¼Å’Ã¥Â¹Â¶Ã¤Â¸â€�Ã¤Â»Â¥7,8Ã¦Ë†â€“9Ã¥Â¼â‚¬Ã¥Â¤Â´Ã£â‚¬â€š
 - Ã§â€�ÂµÃ¨Â¯ï¿½Ã¤Â¿Æ’Ã©â€�â‚¬Ã¥â€˜ËœÃ§Å¡â€žÃ¥ï¿½Â·Ã§Â ï¿½Ã¦Â²Â¡Ã¦Å“â€°Ã¦â€¹Â¬Ã¥ï¿½Â·Ã¦Ë†â€“Ã§Â©ÂºÃ¦Â Â¼ , Ã¤Â½â€ Ã¤Â»Â¥140Ã¥Â¼â‚¬Ã¥Â¤Â´Ã£â‚¬â€š

Ã¨Â¾â€œÃ¥â€¡ÂºÃ¤Â¿Â¡Ã¦ï¿½Â¯:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
Ã¤Â»Â£Ã¥ï¿½Â·Ã¤Â¸ï¿½Ã¨Æ’Â½Ã©â€¡ï¿½Ã¥Â¤ï¿½Ã¯Â¼Å’Ã¦Â¯ï¿½Ã¨Â¡Å’Ã¦â€°â€œÃ¥ï¿½Â°Ã¤Â¸â‚¬Ã¦ï¿½Â¡Ã¯Â¼Å’Ã¦Å’â€°Ã¥Â­â€”Ã¦Â¯ï¿½Ã©Â¡ÂºÃ¥Âºï¿½Ã¨Â¾â€œÃ¥â€¡ÂºÃ£â‚¬â€š

Ã§Â¬Â¬Ã¤ÂºÅ’Ã©Æ’Â¨Ã¥Ë†â€ : Ã§â€�Â±Ã§ï¿½Â­Ã¥Å Â Ã§Â½â€”Ã¥Â°â€�Ã¥â€ºÂºÃ¨Â¯ï¿½Ã¦â€°â€œÃ¥Â¾â‚¬Ã§ï¿½Â­Ã¥Å Â Ã§Â½â€”Ã¥Â°â€�Ã§Å¡â€žÃ§â€�ÂµÃ¨Â¯ï¿½Ã¦â€°â‚¬Ã¥ï¿½Â Ã¦Â¯â€�Ã¤Â¾â€¹Ã¦ËœÂ¯Ã¥Â¤Å¡Ã¥Â°â€˜Ã¯Â¼Å¸
Ã¦ï¿½Â¢Ã¥ï¿½Â¥Ã¨Â¯ï¿½Ã¨Â¯Â´Ã¯Â¼Å’Ã¦â€°â‚¬Ã¦Å“â€°Ã§â€�Â±Ã¯Â¼Ë†080Ã¯Â¼â€°Ã¥Â¼â‚¬Ã¥Â¤Â´Ã§Å¡â€žÃ¥ï¿½Â·Ã§Â ï¿½Ã¦â€¹Â¨Ã¥â€¡ÂºÃ§Å¡â€žÃ©â‚¬Å¡Ã¨Â¯ï¿½Ã¤Â¸Â­Ã¯Â¼Å’
Ã¦â€°â€œÃ¥Â¾â‚¬Ã§â€�Â±Ã¯Â¼Ë†080Ã¯Â¼â€°Ã¥Â¼â‚¬Ã¥Â¤Â´Ã§Å¡â€žÃ¥ï¿½Â·Ã§Â ï¿½Ã¦â€°â‚¬Ã¥ï¿½Â Ã§Å¡â€žÃ¦Â¯â€�Ã¤Â¾â€¹Ã¦ËœÂ¯Ã¥Â¤Å¡Ã¥Â°â€˜Ã¯Â¼Å¸

Ã¨Â¾â€œÃ¥â€¡ÂºÃ¤Â¿Â¡Ã¦ï¿½Â¯:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
Ã¦Â³Â¨Ã¦â€žï¿½Ã¯Â¼Å¡Ã§â„¢Â¾Ã¥Ë†â€ Ã¦Â¯â€�Ã¥Âºâ€�Ã¥Å’â€¦Ã¥ï¿½Â«2Ã¤Â½ï¿½Ã¥Â°ï¿½Ã¦â€¢Â°Ã£â‚¬â€š
"""
#Part I
def search_call_by_Bangalore(input):
    """List all phone numbers called by Bangalore users.

    input: list of calls
    call_by_Bangalore: list. list all area codes called by Bangalore users, include mobile phone and fixed lines
               if phone number is calling number or called number, duration will be added to dictionary value.
    """
    call_by_Bangalore = []
    for element in input:
        #print element
        #print element[0]
        if element[0].startswith("(080)"):
            if element[1].startswith("(0"):
                regx = re.findall(r'[^()]+',element[1])
                #split string with () to list, and use the first element 
                call_by_Bangalore.append(regx[0])
                #append fixed line area code to list
                #print "re.findall(r'[^()]+',element[1]) is {}".format(re.findall(r'[^()]+',element[1]))
                #print "re.findall(r'[^()]+',element[1]) type is {}".format(type(re.findall(r'[^()]+',element[1])))
                #print "phone number: {} call another phone number: {} with area code: {}".format(element[0], element[1], regx[0])
            
            #elif element[1].startswith('7' or '8' or '9') and element[1][5] == ' ':
            else:
                #print "element[1][0-4] is: ".format(element[1][0:5])
                call_by_Bangalore.append(element[1][0:4])
                #append mobile phone number first 5 numbers to list
                #print "phone number: {} call another phone number: {} with area code: {}".format(element[0], element[1], element[1][0:5])
    #print call_by_Bangalore
    call_by_Bangalore_set = set(call_by_Bangalore)
    #transfer list to set to remove same elements
    call_by_Bangalore_list = list(call_by_Bangalore_set)
    #transfer set to list, in order to sort. as set can't be sorted
    call_by_Bangalore_list.sort()
    #print call_by_Bangalore_set
    print ("The number called by people in Bangalore have codes:")
    print '\n'.join(call_by_Bangalore_list)
    return call_by_Bangalore

#search_call_by_Bangalore(calls)

#Part II
def ratio_Bangalore_call_by_Bangalore(input):
    Bangalore_call_by_Bangalore = 0
    for element in input:
        #print element
        if element == "080":
           Bangalore_call_by_Bangalore += 1
           #print "element: {} was called {} times".format(element, Bangalore_call_by_Bangalore)
    ratio = float(Bangalore_call_by_Bangalore*100/len(input))
    print "%.2f%% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." %(ratio)
    
ratio_Bangalore_call_by_Bangalore(search_call_by_Bangalore(calls))
            
   
            