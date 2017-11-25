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
ÃƒÂ¤Ã‚Â»Ã‚Â»ÃƒÂ¥Ã…Â Ã‚Â¡4:
ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¬ÃƒÂ¥Ã¯Â¿Â½Ã‚Â¸ÃƒÂ¥Ã‚Â¸Ã…â€™ÃƒÂ¦Ã…â€œÃ¢â‚¬ÂºÃƒÂ¨Ã‚Â¾Ã‚Â¨ÃƒÂ¨Ã‚Â®Ã‚Â¤ÃƒÂ¥Ã¢â‚¬Â¡Ã‚ÂºÃƒÂ¥Ã¯Â¿Â½Ã‚Â¯ÃƒÂ¨Ã†â€™Ã‚Â½ÃƒÂ¦Ã‚Â­Ã‚Â£ÃƒÂ¥Ã…â€œÃ‚Â¨ÃƒÂ§Ã¢â‚¬ï¿½Ã‚Â¨ÃƒÂ¤Ã‚ÂºÃ…Â½ÃƒÂ¨Ã‚Â¿Ã¢â‚¬ÂºÃƒÂ¨Ã‚Â¡Ã…â€™ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¦Ã…Â½Ã‚Â¨ÃƒÂ©Ã¢â‚¬ï¿½Ã¢â€šÂ¬ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¥Ã¯Â¿Â½Ã‚Â·ÃƒÂ§Ã‚Â Ã¯Â¿Â½ÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
ÃƒÂ¦Ã¢â‚¬Â°Ã‚Â¾ÃƒÂ¥Ã¢â‚¬Â¡Ã‚ÂºÃƒÂ¦Ã¢â‚¬Â°Ã¢â€šÂ¬ÃƒÂ¦Ã…â€œÃ¢â‚¬Â°ÃƒÂ¥Ã¯Â¿Â½Ã‚Â¯ÃƒÂ¨Ã†â€™Ã‚Â½ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¦Ã…Â½Ã‚Â¨ÃƒÂ©Ã¢â‚¬ï¿½Ã¢â€šÂ¬ÃƒÂ¥Ã¢â‚¬ËœÃ‹Å“:
ÃƒÂ¨Ã‚Â¿Ã¢â€žÂ¢ÃƒÂ¦Ã‚Â Ã‚Â·ÃƒÂ§Ã…Â¡Ã¢â‚¬Å¾ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¦Ã¢â€šÂ¬Ã‚Â»ÃƒÂ¦Ã‹Å“Ã‚Â¯ÃƒÂ¥Ã¯Â¿Â½Ã¢â‚¬ËœÃƒÂ¥Ã¢â‚¬Â¦Ã‚Â¶ÃƒÂ¤Ã‚Â»Ã¢â‚¬â€œÃƒÂ¤Ã‚ÂºÃ‚ÂºÃƒÂ¦Ã¢â‚¬Â¹Ã‚Â¨ÃƒÂ¥Ã¢â‚¬Â¡Ã‚ÂºÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¯Ã‚Â¼Ã…â€™
ÃƒÂ¤Ã‚Â½Ã¢â‚¬Â ÃƒÂ¤Ã‚Â»Ã…Â½ÃƒÂ¦Ã¯Â¿Â½Ã‚Â¥ÃƒÂ¤Ã‚Â¸Ã¯Â¿Â½ÃƒÂ¥Ã¯Â¿Â½Ã¢â‚¬ËœÃƒÂ§Ã…Â¸Ã‚Â­ÃƒÂ¤Ã‚Â¿Ã‚Â¡ÃƒÂ£Ã¢â€šÂ¬Ã¯Â¿Â½ÃƒÂ¦Ã…Â½Ã‚Â¥ÃƒÂ¦Ã¢â‚¬ï¿½Ã‚Â¶ÃƒÂ§Ã…Â¸Ã‚Â­ÃƒÂ¤Ã‚Â¿Ã‚Â¡ÃƒÂ¦Ã‹â€ Ã¢â‚¬â€œÃƒÂ¦Ã‹Å“Ã‚Â¯ÃƒÂ¦Ã¢â‚¬ï¿½Ã‚Â¶ÃƒÂ¥Ã‹â€ Ã‚Â°ÃƒÂ¦Ã¯Â¿Â½Ã‚Â¥ÃƒÂ§Ã¢â‚¬ï¿½Ã‚Âµ


ÃƒÂ¨Ã‚Â¯Ã‚Â·ÃƒÂ¨Ã‚Â¾Ã¢â‚¬Å“ÃƒÂ¥Ã¢â‚¬Â¡Ã‚ÂºÃƒÂ¥Ã‚Â¦Ã¢â‚¬Å¡ÃƒÂ¤Ã‚Â¸Ã¢â‚¬Â¹ÃƒÂ¥Ã¢â‚¬Â Ã¢â‚¬Â¦ÃƒÂ¥Ã‚Â®Ã‚Â¹
"These numbers could be telemarketers: "
<list of numbers>
ÃƒÂ§Ã¢â‚¬ï¿½Ã‚ÂµÃƒÂ¨Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¥Ã¯Â¿Â½Ã‚Â·ÃƒÂ§Ã‚Â Ã¯Â¿Â½ÃƒÂ¤Ã‚Â¸Ã¯Â¿Â½ÃƒÂ¨Ã†â€™Ã‚Â½ÃƒÂ©Ã¢â‚¬Â¡Ã¯Â¿Â½ÃƒÂ¥Ã‚Â¤Ã¯Â¿Â½ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¦Ã‚Â¯Ã¯Â¿Â½ÃƒÂ¨Ã‚Â¡Ã…â€™ÃƒÂ¦Ã¢â‚¬Â°Ã¢â‚¬Å“ÃƒÂ¥Ã¯Â¿Â½Ã‚Â°ÃƒÂ¤Ã‚Â¸Ã¢â€šÂ¬ÃƒÂ¦Ã¯Â¿Â½Ã‚Â¡ÃƒÂ¯Ã‚Â¼Ã…â€™ÃƒÂ¦Ã…â€™Ã¢â‚¬Â°ÃƒÂ¥Ã‚Â­Ã¢â‚¬â€�ÃƒÂ¦Ã‚Â¯Ã¯Â¿Â½ÃƒÂ©Ã‚Â¡Ã‚ÂºÃƒÂ¥Ã‚ÂºÃ¯Â¿Â½ÃƒÂ¨Ã‚Â¾Ã¢â‚¬Å“ÃƒÂ¥Ã¢â‚¬Â¡Ã‚ÂºÃƒÂ£Ã¢â€šÂ¬Ã¢â‚¬Å¡
"""

def telemarketers_call_collect(input, input1):
    """List all the possible telemarketers.

    input: list of calls and texts
    telemarketers_call_collect_list: list. list all possible telemarketers phone numbers
               1. Dictonary all call phone numbers to dictionary as key, value is how many times the phone call other numbers.
               2. list all phone numbers as received side, and transfer to set to remove duplacate ones
               3. list all msg sender and msg receiver phone numbers, and transger to set
               4. Traversing all dictionary key, if key is not in list of phone numbers as received side and msg sender and msg receiver side, put it in a new dictionary telemarketers_call_collect
               5. if value of new dictionary bigger thant the average value, it will be saw as a telemarketers phone number, add it to telemarketers_call_collect_list, and sort it
    """
    call_sender = {}
    telemarketers_call_collect = {}
    telemarketers_call_collect_list = []
    call_receiver = []
    msg_sender = []
    msg_receiver = []
    sum = 0    
    for element in input:
        if (element[0] in call_sender):
            call_sender[element[0]] += 1
            call_receiver.append(element[1])
        else:
            call_sender[element[0]] = 1
            call_receiver.append(element[1])

    call_receiver_set = set(call_receiver)
    # Above is the step 1 and step 2

    for element in input1:
        #print "element is {}".format(element)
        #print "element(0) is {}".format(element(0))
        msg_sender.append(element[0])
        msg_receiver.append(element[1])
    
    msg_sender_set = set(msg_sender)
    msg_receiver_set = set(msg_receiver)
    # Above is step 3

    for phone in call_sender:
        if phone in call_receiver_set:
            telemarketers = 0
        elif phone in msg_sender_set:
            telemarketers = 0
        elif phone in msg_receiver_set:
            telemarketers = 0
        else:
            telemarketers_call_collect[phone] = call_sender[phone]
            sum += call_sender[phone]
            #print "phone {} not in the msg and call receive set".format(phone)
    ave = sum/len(telemarketers_call_collect) 
    # Above is step 4
    
    for element in telemarketers_call_collect:
        if telemarketers_call_collect[element] >= ave:
            telemarketers_call_collect_list.append(element)
    telemarketers_call_collect_list.sort()
    # above is step 5
    #print telemarketers_call_collect_list
    print ("These numbers could be telemarketers:")
    print '\n'.join(telemarketers_call_collect_list) 
    return (telemarketers_call_collect_list)

telemarketers_call_collect(calls, texts)
