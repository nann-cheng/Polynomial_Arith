from gmpy2 import powmod

# class polynomial(object):

#TODO: polyExponential
def mod(array,N):
	tmp=[]
	for e in array:
		n=int(e)
		if n<0:
			n+=N
		else:
			n%=N
		tmp.append(n)
	return tmp

def polyReshape(f):
	shaped=[]
	active=False
	for v in f:
		if v!=0 or active:
			shaped.append(v)
			active=True
	return shaped

def polyScaleMul(f,c,N):
	ret = [v*c for v in f]
	return mod(ret,N)

def polyAdd(f,g,N):
	_max = max(len(f),len(g))
	tmp = [0]*_max
	f.reverse()
	g.reverse()
	for i,v in enumerate(f):
		tmp[i] += v
	for i,v in enumerate(g):
		tmp[i] += v
	tmp.reverse()
	return mod(tmp,N)

def polySub(f,g,N):
	g = polyScaleMul(g,-1,N)
	return polyAdd(f,g,N)

def polyMul(f,g,N):
	f = polyReshape(f)
	g = polyReshape(g)
	maxDegree = len(f)+len(g)-1
	tmp=[0] * maxDegree
	for i,v in enumerate(f):
		d1 = len(f)-i-1
		for j,w in enumerate(g):
			d = d1 + len(g)-1-j
			tmp[maxDegree-1 - d] += v*w
	tmp = mod(tmp,N)
	return polyReshape(tmp)

def polyLevelUp(f,level):
	if level>0:
		f += [0] * level
	return f

def polyDiv(f,g,N):
	# assert(len(g) <= len(f),"dim(f) should be GE than dim(g)") In modular
	f = polyReshape(f)
	g = polyReshape(g)

	r = f
	q=[]
	while len(r) > len(q):
		inv=1
		levelUp = len(r)  -   len(g)
		inv = int( powmod(g[0],-1,N) )
		inv = (inv * r[0])%N
		q.append(inv)
		prod = polyLevelUp( polyScaleMul(g,inv,N), levelUp)
		r = polySub(r,prod,N)
		r = polyReshape(r)
	return q,r

# Parameters
# f: a polynomial
# N: the modular field
# Parameters
def polyNormHigh(f,N):
	ret=[]
	if len(f)>0:
		inv = int(powmod(f[0],-1,N))
		for v in f:
			ret.append((v*inv)%N)
	return ret

def PolyGCD(a,b,N):
	q,r = polyDiv(a,b,N)
	# print(r,"\n")
	if r:
		return PolyGCD(b,r,N)
	else:
		return polyNormHigh(b,N)








