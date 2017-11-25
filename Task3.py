#-*- coding:utf-8 -*- 
"""
ä¸‹é�¢çš„æ–‡ä»¶å°†ä¼šä»Žcsvæ–‡ä»¶ä¸­è¯»å�–è¯»å�–çŸ­ä¿¡ä¸Žç”µè¯�è®°å½•ï¼Œ
ä½ å°†åœ¨ä»¥å�Žçš„è¯¾ç¨‹ä¸­äº†è§£æ›´å¤šæœ‰å…³è¯»å�–æ–‡ä»¶çš„çŸ¥è¯†ã€‚
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
ä»»åŠ¡3:
(080)æ˜¯ç�­åŠ ç½—å°”çš„å›ºå®šç”µè¯�åŒºå�·ã€‚
å›ºå®šç”µè¯�å�·ç �åŒ…å�«æ‹¬å�·ï¼Œ
æ‰€ä»¥ç�­åŠ ç½—å°”åœ°åŒºçš„ç”µè¯�å�·ç �çš„æ ¼å¼�ä¸º(080)xxxxxxxã€‚

ç¬¬ä¸€éƒ¨åˆ†: æ‰¾å‡ºè¢«ç�­åŠ ç½—å°”åœ°åŒºçš„å›ºå®šç”µè¯�æ‰€æ‹¨æ‰“çš„æ‰€æœ‰ç”µè¯�çš„åŒºå�·å’Œç§»åŠ¨å‰�ç¼€ï¼ˆä»£å�·ï¼‰ã€‚
 - å›ºå®šç”µè¯�ä»¥æ‹¬å�·å†…çš„åŒºå�·å¼€å§‹ã€‚åŒºå�·çš„é•¿åº¦ä¸�å®šï¼Œä½†æ€»æ˜¯ä»¥ 0 æ‰“å¤´ã€‚
 - ç§»åŠ¨ç”µè¯�æ²¡æœ‰æ‹¬å�·ï¼Œä½†æ•°å­—ä¸­é—´æ·»åŠ äº†
   ä¸€ä¸ªç©ºæ ¼ï¼Œä»¥å¢žåŠ å�¯è¯»æ€§ã€‚ä¸€ä¸ªç§»åŠ¨ç”µè¯�çš„ç§»åŠ¨å‰�ç¼€æŒ‡çš„æ˜¯ä»–çš„å‰�å››ä¸ª
   æ•°å­—ï¼Œå¹¶ä¸”ä»¥7,8æˆ–9å¼€å¤´ã€‚
 - ç”µè¯�ä¿ƒé”€å‘˜çš„å�·ç �æ²¡æœ‰æ‹¬å�·æˆ–ç©ºæ ¼ , ä½†ä»¥140å¼€å¤´ã€‚

è¾“å‡ºä¿¡æ�¯:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
ä»£å�·ä¸�èƒ½é‡�å¤�ï¼Œæ¯�è¡Œæ‰“å�°ä¸€æ�¡ï¼ŒæŒ‰å­—æ¯�é¡ºåº�è¾“å‡ºã€‚

ç¬¬äºŒéƒ¨åˆ†: ç”±ç�­åŠ ç½—å°”å›ºè¯�æ‰“å¾€ç�­åŠ ç½—å°”çš„ç”µè¯�æ‰€å� æ¯”ä¾‹æ˜¯å¤šå°‘ï¼Ÿ
æ�¢å�¥è¯�è¯´ï¼Œæ‰€æœ‰ç”±ï¼ˆ080ï¼‰å¼€å¤´çš„å�·ç �æ‹¨å‡ºçš„é€šè¯�ä¸­ï¼Œ
æ‰“å¾€ç”±ï¼ˆ080ï¼‰å¼€å¤´çš„å�·ç �æ‰€å� çš„æ¯”ä¾‹æ˜¯å¤šå°‘ï¼Ÿ

è¾“å‡ºä¿¡æ�¯:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
æ³¨æ„�ï¼šç™¾åˆ†æ¯”åº”åŒ…å�«2ä½�å°�æ•°ã€‚
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
            elif element[1].startswith('7' or '8' or '9') and element[1][5] == ' ':
                #print "element[1][0-4] is: ".format(element[1][0:5])
                call_by_Bangalore.append(element[1][0:5])
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
            
   
            