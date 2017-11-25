#-*- coding:utf-8 -*- 
"""
Ã¤Â¸â€¹Ã©ï¿½Â¢Ã§Å¡â€žÃ¦â€“â€¡Ã¤Â»Â¶Ã¥Â°â€ Ã¤Â¼Å¡Ã¤Â»Å½csvÃ¦â€“â€¡Ã¤Â»Â¶Ã¤Â¸Â­Ã¨Â¯Â»Ã¥ï¿½â€“Ã¨Â¯Â»Ã¥ï¿½â€“Ã§Å¸Â­Ã¤Â¿Â¡Ã¤Â¸Å½Ã§â€�ÂµÃ¨Â¯ï¿½Ã¨Â®Â°Ã¥Â½â€¢Ã¯Â¼Å’
Ã¤Â½Â Ã¥Â°â€ Ã¥Å“Â¨Ã¤Â»Â¥Ã¥ï¿½Å½Ã§Å¡â€žÃ¨Â¯Â¾Ã§Â¨â€¹Ã¤Â¸Â­Ã¤Âºâ€ Ã¨Â§Â£Ã¦â€ºÂ´Ã¥Â¤Å¡Ã¦Å“â€°Ã¥â€¦Â³Ã¨Â¯Â»Ã¥ï¿½â€“Ã¦â€“â€¡Ã¤Â»Â¶Ã§Å¡â€žÃ§Å¸Â¥Ã¨Â¯â€ Ã£â‚¬â€š
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
Ã¤Â»Â»Ã¥Å Â¡1Ã¯Â¼Å¡
Ã§Å¸Â­Ã¤Â¿Â¡Ã¥â€™Å’Ã©â‚¬Å¡Ã¨Â¯ï¿½Ã¨Â®Â°Ã¥Â½â€¢Ã¤Â¸Â­Ã¤Â¸â‚¬Ã¥â€¦Â±Ã¦Å“â€°Ã¥Â¤Å¡Ã¥Â°â€˜Ã§â€�ÂµÃ¨Â¯ï¿½Ã¥ï¿½Â·Ã§Â ï¿½Ã¯Â¼Å¸Ã¦Â¯ï¿½Ã¤Â¸ÂªÃ¥ï¿½Â·Ã§Â ï¿½Ã¥ï¿½ÂªÃ§Â»Å¸Ã¨Â®Â¡Ã¤Â¸â‚¬Ã¦Â¬Â¡Ã£â‚¬â€š
Ã¨Â¾â€œÃ¥â€¡ÂºÃ¤Â¿Â¡Ã¦ï¿½Â¯Ã¯Â¼Å¡
"There are <count> different telephone numbers in the records."
"""


def collect_phone_number(input):
    phone_num = []
    for element in input:
        phone_num.append(element[0])
        phone_num.append(element[1])
    return phone_num

def remove_duplecates(input):
    phone_num = []
    for element in input:
        if element not in phone_num:
            phone_num.append(element)
    return phone_num

phone_texts_calls = texts + calls

phone = remove_duplecates(collect_phone_number(phone_texts_calls))

print "There are {} different telephone numbers in the records.".format(len(phone))

"""
def phone_num_count(phone_nums):
    phone_num_count = {}
    for phone_num in phone_nums:
        if phone_num in phone_num_count:
            phone_num_count[phone_num] += 1
        else:
            phone_num_count[phone_num] = 1
    return phone_num_count

def phone_count_max(phone_num_count):
    phone_count_max = {}
    maxnum = 0
    for phone_num in phone_num_count:
        if phone_num_count[phone_num] >= maxnum:
            maxnum = phone_num_count[phone_num]
            phone_count_max[phone_num] = maxnum
    if len(phone_count_max) == 1:
        print "There are {} different "

phone_texts_calls = texts + calls

phone = phone_num_count(collect_phone_number(phone_texts_calls))

print phone
"""