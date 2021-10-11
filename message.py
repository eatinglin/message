
data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#字的計數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1

while True:
	ask = input('請問要查詢的字為： ')
	if ask == 'q':
		break
	if ask not in wc:
		print('沒有這個字')
	else:
		print(ask, '這個字出現過', wc[ask], '次')
print('感謝使用本查詢功能')


# for word in wc:
# 	if wc[word] > 1000000:
# 		print(word, wc[word])








#算留言平均長度


# number = 0
# for word in data:
# 	number += len(word)
# print('留言平均長度為', number/len(data))


# new = []
# for word in data:
# 	if len(word) < 100:
# 		new.append(word)
# print('共有', len(new), '筆留言小於100字')

# good = []
# for word in data:
# 	if 'good' in word:
# 		good.append(word)
# print('共有', len(good), '筆留言提到good')
# print(good[0])

# # good = [d for d in data if 'good' in d]
# bad = ['bad' in d for d in data]




"""
word = 'Hi, new world'

for w in word:
	print(w)
"""