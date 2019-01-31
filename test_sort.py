def bubble_sort(a):
	"""сортировка списка a методом пузырька"""
	for x1 in range(1,len(a)):
		for x2 in range(0,len(a)-x1):
			if a[x2]>a[x2+1]:
				a[x2],a[x2+1]=a[x2+1],a[x2]
	x1+=1

def insert_sort(a):
	"""сортировка списка a методом сортировки"""
	for x1 in range(1,len(a)):
		x2=x1
		while x2>0 and a[x2-1]>a[x2]:
			a[x2-1],a[x2]=[x2],a[x2-1]
			x2 -=1
			
def choise_sort(a):
	"""сортировка списка a методом выбора"""
	for x1 in range (0,len(a)-1):
		for x2 in range (x1+1,len(a)):
			if a[x2]<a[x1]:
				a[x2],a[x1]=a[x1],a[x2]

def test_sort(sort_algoritm):
	print('test 1:',sort_algoritm.__doc__,end = '\t ')
	a=[9,8,7,6,5,4,3,2,1]
	a_sort=[1,2,3,4,5,6,7,8,9]
	sort_algoritm(a)
	print('ok' if a==a_sort else 'off')
	print(a)
	print(a_sort)
	

if __name__ == '__main__':
	test_sort(bubble_sort)
	test_sort(insert_sort)
	test_sort(choise_sort)


