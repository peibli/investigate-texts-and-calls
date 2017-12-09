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
Ã¤Â»Â»Ã¥Å Â¡0:
Ã§Å¸Â­Ã¤Â¿Â¡Ã¨Â®Â°Ã¥Â½â€¢Ã§Å¡â€žÃ§Â¬Â¬Ã¤Â¸â‚¬Ã¦ï¿½Â¡Ã¨Â®Â°Ã¥Â½â€¢Ã¦ËœÂ¯Ã¤Â»â‚¬Ã¤Â¹Ë†Ã¯Â¼Å¸Ã©â‚¬Å¡Ã¨Â¯ï¿½Ã¨Â®Â°Ã¥Â½â€¢Ã¦Å“â‚¬Ã¥ï¿½Å½Ã¤Â¸â‚¬Ã¦ï¿½Â¡Ã¨Â®Â°Ã¥Â½â€¢Ã¦ËœÂ¯Ã¤Â»â‚¬Ã¤Â¹Ë†Ã¯Â¼Å¸
Ã¨Â¾â€œÃ¥â€¡ÂºÃ¤Â¿Â¡Ã¦ï¿½Â¯:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#Task 0
print ("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))
print ("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))