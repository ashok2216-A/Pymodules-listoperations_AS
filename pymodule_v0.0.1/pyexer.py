def swap_list(listed):

	size = len(listed) #10
	swaped = listed[0]
	listed[0] = listed[size - 1]
	listed[size - 1] = swaped

	return listed

print(swap_list([1,'2,3,4,5,6,7,8',9,10]))
print('-'*80)

def swap_2list(listed):

	size = len(listed)
	temp_list = [1,2,3,'4,5,6,7',8,9,10]
	listed[0], listed[1] = listed[size - 1], listed[size - 2]
	listed[size - 1], listed[size - 2] = [temp_list[0], temp_list[1]]
	return listed

print(swap_2list([1,2,[["3,4"],"5,6,7,8"],9,10]))
print('-'*80)

def swap_letter(string, replacewhat, replacethat):

		replaced = string.replace(str(replacewhat), str(replacethat))
		print('Previous word: %s' % string)
		print('After Replaced: %s' % replaced)
		return replaced

print(swap_letter('ASHOK ', ' ', 'KUMAR'))
print('-'*80)

def lntOFlst(urlist):

		counter = 0
		for i in urlist:
			counter = counter + 1
		print('Length of list is %s' % str(counter))
		return counter

print(lntOFlst([1,2,('3',4,5)]))
print('-'*80)

def maxnum(x, y):

	if x > y:
		print('%s is Max' % x)
	elif y > x:
		print('%s is Max' % y)
	return x, y

print(maxnum(5,20))
print('-'*80)

def minnum(x, y):
	
	if x < y:
		print('%s is Min' % x)
	elif y < x:
		print('%s is Min' % y)
	return x, y

print(minnum(5,20))
print('-'*80)

def checklst(urlist, checkwhat):

	if checkwhat in urlist:
		print('Yes %s it is in the list' % checkwhat)
	return urlist

print(checklst([1,2,3,4,5,6,7,8,9,10], 5))
print('-'*80)

def clrlst(lists, cmd):

	if cmd == "clearlist":
		lists = []
	return lists
a = [10,20,30,40,50,60,70,80,90,100]

print(clrlst(a, 'clearlist'))
print('-'*80)

def revlist(urlist):

	revelist = urlist[::-1]
	return revelist
a = ['a', 'b', (5,6,7),'f', '5']
print(revlist(a))
print('-'*80)

def copylst(lstcpyfrm, lstcpyto):
	
	if lstcpyto == list(lstcpyto):
		lstcpyto = lstcpyfrm
		if lstcpyfrm != list(lstcpyfrm):
			print('Error: Copy from- it is Not a list')
	else:
		print("ERROR: Copy to- it's Not a list")
	return lstcpyto
a = [1,6,5,8,2,5,4]
b = [0,1]
c = ()
print(copylst(a, b))
print(copylst(a,c))
print('-'*80)


def repetedlements(lists, value):

	count = 0
	for lsts in lists: 
		if value == lsts:
			count = count + 1
	print('The element {0} is occured {1} Times'.format(value, count))

	return count

a = [1,2,5,5,3,4,5,8,9,7,5,10]
print(repetedlements(a, 5))
print('-'*80)

# Python program to find the sum
# and average of the list

L = [4, 5, 1, 2, 9, 7, 10, 8]

def sumof(lists):

	global count
	count = 0
	for i in lists:
		count = count + i	
		sumof = count
	return sumof

def avgof(lists):

	avgof = count /len(lists)

	return avgof
 
print(sumof(L))
print(avgof(L))
print('-'*80)

test_list = [12, 67, 98, 34]

print("The original list is : " + str(test_list))

res = []
for ele in test_list:
	sum = 0
	for digit in str(ele):
		sum += int(digit)
	res.append(sum)
	
print ("List Integer Summation : " + str(res))
print('-' *80)

def rmvMtLst(urlist):

	nulist = list(filter(None, urlist))
	return nulist

print(rmvMtLst([1,2,3,[],1,2]))
print('-'*80)


def cvtlstTOdist(keylist, testlists):

	lstdist = []
	ranges = len(keylist)
	for idx in range(0,len(keylist)):
		keys = keylist[idx]
		value = testlists[idx]
		mrglst = {keys:value}
		lstdist.append(mrglst)

	return lstdist
		
print(cvtlstTOdist([1,2,3,4,5], ['a', 'b', 'c', 'd', 'e']))
print('-'*80)

def uncommon(lists1, lists2):

	res_list = []
	for i in lists1:
		if i not in lists2:
			res_list.append(i)
	for i in lists2:
		if i not in lists1:
			res_list.append(i)

	return res_list

print(uncommon([1,2,3,4], [1,5,4,6]))
print('-'*80)



def randlst(lists):
	import random
	lists = random.choice(lists)

	return lists

print(randlst([5,9,6,1,4,7,2,5,6]))

