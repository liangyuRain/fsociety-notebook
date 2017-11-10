import time


def solution(s):
    s = [ord(ch) - ord('a') for ch in s]
    opt = [s[i] for i in range(len(s))]
    for j in range(len(s)):
        ptr = s[j] - 1
        for i in reversed(range(j)):
            if s[i] < s[j]:
                opt[j] = min(opt[j], opt[i] + max(0, ptr - s[i]))
                if s[i] == ptr:
                    ptr -= 1
    ptr = 25
    minCost = 26
    for j in reversed(range(len(s))):
        minCost = min(minCost, opt[j] + max(0, ptr - s[j]))
        if s[j] == ptr:
            ptr -= 1
    return minCost


for i in range(1000, 2003):
	try:
		with open('input/Alphabet-{0}.in'.format(i)) as f_in:
			s = f_in.readline()
			start = time.time()
			v = solution(s)
			end = time.time()
			with open('output/Alphabet-{0}.out'.format(i)) as f_out:
				ex = int(f_out.readline())
				if ex != v:
					print('{0}\tgiven: {1}\texpected: {2}'.format(i, v, ex))
				else:
					print('{0}\tpassed'.format(i))
			if end - start > 1:
				print('{0}\ttime: {1}'.format(i, end - start))
	except:
		pass
		
		
		
