#-*- coding:utf-8 -*- 
"""
ä¸‹é�¢çš„æ–‡ä»¶å°†ä¼šä»Žcsvæ–‡ä»¶ä¸­è¯»å�–è¯»å�–çŸ­ä¿¡ä¸Žç”µè¯�è®°å½•ï¼Œ
ä½ å°†åœ¨ä»¥å�Žçš„è¯¾ç¨‹ä¸­äº†è§£æ›´å¤šæœ‰å…³è¯»å�–æ–‡ä»¶çš„çŸ¥è¯†ã€‚
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
ä»»åŠ¡0:
çŸ­ä¿¡è®°å½•çš„ç¬¬ä¸€æ�¡è®°å½•æ˜¯ä»€ä¹ˆï¼Ÿé€šè¯�è®°å½•æœ€å�Žä¸€æ�¡è®°å½•æ˜¯ä»€ä¹ˆï¼Ÿ
è¾“å‡ºä¿¡æ�¯:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#Task 0
print "First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2])
print "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3])