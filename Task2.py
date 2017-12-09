#-*- coding:utf-8 -*- 
"""
ÃƒÂ¤Ã‚Â¸Ã¢â‚¬Â¹ÃƒÂ©Ã¯Â¿Â½Ã‚Â¢ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¦Ã¢â‚¬â€œÃ¢â‚¬Â¡ÃƒÂ¤Ã‚Â»Ã‚Â¶ÃƒÂ¥Ã‚Â°Ã¢â‚¬Â ÃƒÂ¤Ã‚Â¼Ã…Â¡ÃƒÂ¤Ã‚Â»Ã…Â½csvÃƒÂ¦Ã¢â‚¬â€œÃ¢â‚¬Â¡ÃƒÂ¤Ã‚Â»Ã‚Â¶ÃƒÂ¤Ã‚Â¸Ã‚Â­ÃƒÂ¨Ã‚Â¯Ã‚Â»ÃƒÂ¥Ã¯Â¿Â½Ã¢â‚¬â€œÃƒÂ¨Ã‚Â¯Ã‚Â»ÃƒÂ¥Ã¯Â¿Â½Ã¢â‚¬â€œÃƒÂ§Ã…Â¸Ã‚Â­ÃƒÂ¤Ã‚Â¿Ã‚Â¡ÃƒÂ¤Ã‚Â¸Ã…Â½ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¨Ã‚Â®Ã‚Â°ÃƒÂ¥Ã‚Â½Ã¢â‚¬Â¢ÃƒÂ¯Ã‚Â¼Ã…â€™
ÃƒÂ¤Ã‚Â½Ã‚Â ÃƒÂ¥Ã‚Â°Ã¢â‚¬Â ÃƒÂ¥Ã…â€œÃ‚Â¨ÃƒÂ¤Ã‚Â»Ã‚Â¥ÃƒÂ¥Ã¯Â¿Â½Ã…Â½ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¨Ã‚Â¯Ã‚Â¾ÃƒÂ§Ã‚Â¨Ã¢â‚¬Â¹ÃƒÂ¤Ã‚Â¸Ã‚Â­ÃƒÂ¤Ã‚ÂºÃ¢â‚¬Â ÃƒÂ¨Ã‚Â§Ã‚Â£ÃƒÂ¦Ã¢â‚¬ÂºÃ‚Â´ÃƒÂ¥Ã‚Â¤Ã…Â¡ÃƒÂ¦Ã…â€œÃ¢â‚¬Â°ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â³ÃƒÂ¨Ã‚Â¯Ã‚Â»ÃƒÂ¥Ã¯Â¿Â½Ã¢â‚¬â€œÃƒÂ¦Ã¢â‚¬â€œÃ¢â‚¬Â¡ÃƒÂ¤Ã‚Â»Ã‚Â¶ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ§Ã…Â¸Ã‚Â¥ÃƒÂ¨Ã‚Â¯Ã¢â‚¬Â ÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
ÃƒÂ¤Ã‚Â»Ã‚Â»ÃƒÂ¥Ã…Â Ã‚Â¡2: ÃƒÂ¥Ã¢â‚¬Å“Ã‚ÂªÃƒÂ¤Ã‚Â¸Ã‚ÂªÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¥Ã¯Â¿Â½Ã‚Â·ÃƒÂ§Ã‚Â Ã¯Â¿Â½ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ©Ã¢â€šÂ¬Ã…Â¡ÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¦Ã¢â€šÂ¬Ã‚Â»ÃƒÂ¦Ã¢â‚¬â€�Ã‚Â¶ÃƒÂ©Ã¢â‚¬â€�Ã‚Â´ÃƒÂ¦Ã…â€œÃ¢â€šÂ¬ÃƒÂ©Ã¢â‚¬Â¢Ã‚Â¿? ÃƒÂ¤Ã‚Â¸Ã¯Â¿Â½ÃƒÂ¨Ã‚Â¦Ã¯Â¿Â½ÃƒÂ¥Ã‚Â¿Ã‹Å“ÃƒÂ¨Ã‚Â®Ã‚Â°ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ§Ã¢â‚¬ï¿½Ã‚Â¨ÃƒÂ¤Ã‚ÂºÃ…Â½ÃƒÂ¦Ã…Â½Ã‚Â¥ÃƒÂ¥Ã¯Â¿Â½Ã‚Â¬ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¦Ã¢â‚¬â€�Ã‚Â¶ÃƒÂ©Ã¢â‚¬â€�Ã‚Â´ÃƒÂ¤Ã‚Â¹Ã…Â¸ÃƒÂ¦Ã‹Å“Ã‚Â¯ÃƒÂ©Ã¢â€šÂ¬Ã…Â¡ÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¦Ã¢â‚¬â€�Ã‚Â¶ÃƒÂ©Ã¢â‚¬â€�Ã‚Â´ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¤Ã‚Â¸Ã¢â€šÂ¬ÃƒÂ©Ã†â€™Ã‚Â¨ÃƒÂ¥Ã‹â€ Ã¢â‚¬Â ÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
ÃƒÂ¨Ã‚Â¾Ã¢â‚¬Å“ÃƒÂ¥Ã¢â‚¬Â¡Ã‚ÂºÃƒÂ¤Ã‚Â¿Ã‚Â¡ÃƒÂ¦Ã¯Â¿Â½Ã‚Â¯:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

ÃƒÂ¦Ã¯Â¿Â½Ã¯Â¿Â½ÃƒÂ§Ã‚Â¤Ã‚Âº: ÃƒÂ¥Ã‚Â»Ã‚ÂºÃƒÂ§Ã‚Â«Ã¢â‚¬Â¹ÃƒÂ¤Ã‚Â¸Ã¢â€šÂ¬ÃƒÂ¤Ã‚Â¸Ã‚ÂªÃƒÂ¥Ã‚Â­Ã¢â‚¬â€�ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¸ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¥Ã‚Â¹Ã‚Â¶ÃƒÂ¤Ã‚Â»Ã‚Â¥ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¥Ã¯Â¿Â½Ã‚Â·ÃƒÂ§Ã‚Â Ã¯Â¿Â½ÃƒÂ¤Ã‚Â¸Ã‚ÂºÃƒÂ©Ã¢â‚¬ï¿½Ã‚Â®ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ©Ã¢â€šÂ¬Ã…Â¡ÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¦Ã¢â€šÂ¬Ã‚Â»ÃƒÂ¦Ã¢â‚¬â€�Ã‚Â¶ÃƒÂ©Ã¢â‚¬Â¢Ã‚Â¿ÃƒÂ¤Ã‚Â¸Ã‚ÂºÃƒÂ¥Ã¢â€šÂ¬Ã‚Â¼ÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
ÃƒÂ¨Ã‚Â¿Ã¢â€žÂ¢ÃƒÂ¦Ã…â€œÃ¢â‚¬Â°ÃƒÂ¥Ã‹â€ Ã‚Â©ÃƒÂ¤Ã‚ÂºÃ…Â½ÃƒÂ¤Ã‚Â½Ã‚Â ÃƒÂ§Ã‚Â¼Ã¢â‚¬â€œÃƒÂ¥Ã¢â‚¬Â Ã¢â€žÂ¢ÃƒÂ¤Ã‚Â¸Ã¢â€šÂ¬ÃƒÂ¤Ã‚Â¸Ã‚ÂªÃƒÂ¤Ã‚Â»Ã‚Â¥ÃƒÂ©Ã¢â‚¬ï¿½Ã‚Â®ÃƒÂ¥Ã¢â€šÂ¬Ã‚Â¼ÃƒÂ¥Ã‚Â¯Ã‚Â¹ÃƒÂ¤Ã‚Â¸Ã‚ÂºÃƒÂ¨Ã‚Â¾Ã¢â‚¬Å“ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¥ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¥Ã‚Â¹Ã‚Â¶ÃƒÂ¤Ã‚Â¿Ã‚Â®ÃƒÂ¦Ã¢â‚¬ï¿½Ã‚Â¹ÃƒÂ¥Ã‚Â­Ã¢â‚¬â€�ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¸ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¥Ã¢â‚¬Â¡Ã‚Â½ÃƒÂ¦Ã¢â‚¬Â¢Ã‚Â°ÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
ÃƒÂ¥Ã‚Â¦Ã¢â‚¬Å¡ÃƒÂ¦Ã…Â¾Ã…â€œÃƒÂ©Ã¢â‚¬ï¿½Ã‚Â®ÃƒÂ¥Ã‚Â·Ã‚Â²ÃƒÂ§Ã‚Â»Ã¯Â¿Â½ÃƒÂ¥Ã‚Â­Ã‹Å“ÃƒÂ¥Ã…â€œÃ‚Â¨ÃƒÂ¤Ã‚ÂºÃ…Â½ÃƒÂ¥Ã‚Â­Ã¢â‚¬â€�ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¸ÃƒÂ¥Ã¢â‚¬Â Ã¢â‚¬Â¦ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¤Ã‚Â¸Ã‚ÂºÃƒÂ©Ã¢â‚¬ï¿½Ã‚Â®ÃƒÂ¦Ã¢â‚¬Â°Ã¢â€šÂ¬ÃƒÂ¥Ã‚Â¯Ã‚Â¹ÃƒÂ¥Ã‚ÂºÃ¢â‚¬ï¿½ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¥Ã¢â€šÂ¬Ã‚Â¼ÃƒÂ¥Ã…Â Ã‚Â ÃƒÂ¤Ã‚Â¸Ã…Â ÃƒÂ¥Ã‚Â¯Ã‚Â¹ÃƒÂ¥Ã‚ÂºÃ¢â‚¬ï¿½ÃƒÂ¦Ã¢â‚¬Â¢Ã‚Â°ÃƒÂ¥Ã¢â€šÂ¬Ã‚Â¼ÃƒÂ¯Ã‚Â¼Ã¢â‚¬Âº
ÃƒÂ¥Ã‚Â¦Ã¢â‚¬Å¡ÃƒÂ¦Ã…Â¾Ã…â€œÃƒÂ©Ã¢â‚¬ï¿½Ã‚Â®ÃƒÂ¤Ã‚Â¸Ã¯Â¿Â½ÃƒÂ¥Ã‚Â­Ã‹Å“ÃƒÂ¥Ã…â€œÃ‚Â¨ÃƒÂ¤Ã‚ÂºÃ…Â½ÃƒÂ¥Ã‚Â­Ã¢â‚¬â€�ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¸ÃƒÂ¥Ã¢â‚¬Â Ã¢â‚¬Â¦ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¥Ã‚Â°Ã¢â‚¬Â ÃƒÂ¦Ã‚Â­Ã‚Â¤ÃƒÂ©Ã¢â‚¬ï¿½Ã‚Â®ÃƒÂ¥Ã…Â Ã‚Â ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¥ÃƒÂ¥Ã‚Â­Ã¢â‚¬â€�ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¸ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¥Ã‚Â¹Ã‚Â¶ÃƒÂ¥Ã‚Â°Ã¢â‚¬Â ÃƒÂ¥Ã‚Â®Ã†â€™ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ¥Ã¢â€šÂ¬Ã‚Â¼ÃƒÂ¨Ã‚Â®Ã‚Â¾ÃƒÂ¤Ã‚Â¸Ã‚ÂºÃƒÂ§Ã‚Â»Ã¢â€žÂ¢ÃƒÂ¥Ã‚Â®Ã…Â¡ÃƒÂ¥Ã¢â€šÂ¬Ã‚Â¼ÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
"""
#print calls[0]

def collect_phone_number(input):
    """List all phone numbers and durations.

    input: list of calls
    phone_num: dictionary. key is phone number, value is duration
               if phone number is calling number or called number, duration will be added to dictionary value.
    """
    phone_num = {}
    for element in input:
        if (element[0] in phone_num):
            phone_num[element[0]] += int(element[3])
        else:
            phone_num[element[0]] = int(element[3])
        if (element[1] in phone_num):
            phone_num[element[1]] += int(element[3])
        else:
            phone_num[element[1]] = int(element[3])
            #print "element is {}, and call duration is {}".format(element[1], element[3])
    #print phone_num
    return phone_num

"""
def phone_call_time_max(phone_num):
    put the longest duration call's phone number and duration put it into phone_call_time_max list.

    input: dic. phone number and duration
    phone_call_time_max: list, include the longest duration call's phone numbers and value
               of course maybe there are more than two calls have the same longest duration, considered also
    
    phone_call_time_max = [0,0]
    maxnum = 0
    #print phone_num
    for element in phone_num:
        #print "phone_num's element is {}".format(element)
        if phone_num[element] > maxnum:
            #print "phone_num's element {} value {} more than the maxnum {} value".format(element, phone_num[element], maxnum)
            maxnum = phone_num[element]
            phone_call_time_max[0] = element 
            phone_call_time_max[1] = maxnum 
            #phone number location is 0, duration is 1         
    print "{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_call_time_max[0], phone_call_time_max[-1])              
    return phone_call_time_max 

phone_call_time_max(collect_phone_number(calls))
"""

phone_num = collect_phone_number(calls)
key,value = max(phone_num.items(), key=lambda x:x[1])
print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, value))