
data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#算留言平均長度


number = 0
for word in data:
	number += len(word)
print('留言平均長度為', number/len(data))


new = []
for word in data:
	if len(word) < 100:
		new.append(word)
print('共有', len(new), '筆留言小於100字')



"""
word = 'Hi, new world'

for w in word:
	print(w)
"""