def magic(s):
	possible = [
			[4,9,2,3,5,7,8,1,6],
			[4,3,8,9,5,1,2,7,6],
            [2,9,4,7,5,3,6,1,8],
            [2,7,6,9,5,1,4,3,8],
            [8,1,6,3,5,7,4,9,2],
            [8,3,4,1,5,9,6,7,2],
            [6,7,2,1,5,9,8,3,4],
            [6,1,8,7,5,3,2,9,4]
        ]
	t=0
	for i in range(8):
		c = 0
		for j in range(3):
			for k in range(3):
				c=c+abs(possible[i][3*j+k]-s[j][k])
				if i==0:t=c
		if c<t:
			t=c
	
	return t

def main():
	s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
	res = magic(s)
	print(res)

if __name__ == '__main__':
	main()