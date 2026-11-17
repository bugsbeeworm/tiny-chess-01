c=StopIteration
E=range
Q=enumerate
M=ord
L=abs
import os,random as a,urllib.request as e,json as I
O=3e4
U=0,100,320,330,500,900,0
d='::::;<<6;98::::>;;<?<<>@DDDD::::024426:;4;<=4:=>4;=>4:<=26::0244'
f=[M(A)*5-290 for A in d]
B=[0]*128
for(D,S)in Q([4,2,3,5,6,3,2,4]):B[D]=S;B[16+D]=1;B[112+D]=-S;B[96+D]=-1
g=B[:]
A=1
F=15
G=-1
H=[4,116]
C=0
T={4:3,7:1,0:2,116:12,119:4,112:8}
h='PTac40#!QS31BBBBCRA2BBBBCQRSA321CQRSA321'
i=a.Random(1)
Y=i.getrandbits
R=[[Y(64)for A in E(128)]for A in E(13)]
j=Y(64)
P={}
V=[0]
k=9e4
def l():global A,F,G,C;B[:]=g;A=1;F=15;G=-1;H[:]=4,116;C=0
def K(t,by):
	for(E,F)in zip('31PTac40#!CQRSA321','112222222266666666'):
		A=t+(M(E)-66)*by
		if not A&136 and B[A]==by*(M(F)-48):return 1
	for C in(1,15,16,17,-1,-15,-16,-17):
		A=t+C
		while not A&136:
			D=B[A]
			if D:
				if D==by*5 or D==by*(3 if L(C)in(15,17)else 4):return 1
				break
			A+=C
	return 0
def W():
	N=[]
	for(E,P)in Q(B):
		if P*A<=0:continue
		O=L(P)
		if O==1:
			for R in(16,15,17):
				C=E+R*A;S=R!=16
				if C&136:continue
				I=B[C]
				if S:
					if not I and C!=G:continue
					if I and I*A>0:continue
					T=1+4*(not I)
				else:
					if I:continue
					T=0
				for U in(5,4,3,2)if C>>4 in(0,7)else(0,):N.append((E,C,U,T))
				if not S and E>>4==(A<0)*5+1 and not B[E+32*A]:N.append((E,E+32*A,0,2))
		else:
			for V in h[(O-2)*8:(O-1)*8]:
				D=M(V)-66;C=E+D
				while not C&136:
					I=B[C]
					if not I:N.append((E,C,0,0))
					else:
						if I*A<0:N.append((E,C,0,1))
						break
					if O%4==2:break
					C+=D
			if O==6:
				J=H[(1-A)//2]
				for D in(1,-1):
					if F&(3-D)//2<<(A<0)*2 and not B[J+D]|B[J+2*D]|(D<0)*B[J-3]and not(K(J,-A)or K(J+D,-A)or K(J+2*D,-A)):N.append((J,J+2*D,0,8))
	return N
def Z():
	B=[]
	for C in W():
		D=J(C)
		if not K(H[(1+A)//2],A):B.append(C)
		N(D)
	return B
def J(m):
	global A,F,G,C;E,D,N,I=m;J=B[E];K=B[D];M=D
	if I&4:M=D-16*A;K=-A
	O=N*A if N else J;P=m,K,M,F,G,J,C;C^=R[J+6][E]^R[O+6][D]
	if K:C^=R[K+6][M]
	if I&4:B[M]=0
	B[E]=0;B[D]=O
	if I&8:B[D+(-1 if D&7>4 else 1)]=4*A;B[D+(1 if D&7>4 else-2)]=0
	if L(J)==6:H[(1-A)//2]=D
	F&=~(T.get(E,0)|T.get(D,0));G=D-16*A if I&2 else-1;C^=j;A=-A;return P
def N(u):
	global A,F,G,C;M,E,N,F,G,I,C=u;J,D,O,K=M;A=-A;B[J]=I
	if K&4:B[N]=E;B[D]=0
	else:B[D]=E
	if K&8:B[D+(1 if D&7>4 else-2)]=4*A;B[D+(-1 if D&7>4 else 1)]=0
	if L(I)==6:H[(1-A)//2]=J
def b():
	E=0
	for(F,C)in Q(B):
		if not C:continue
		D=L(C);G=F&7;H=F>>4;I=U[D]+(f[(H if C>0 else 7-H)*4+min(G,7-G)+(D-1)*32]if D<3 else 0);E+=I if C>0 else-I
	return E*A
def X(a,be,d,pl):
	M=pl;E=be;V[0]+=1
	if V[0]>k:raise c
	if M>20:return b()
	if d<=0 and not K(H[(1-A)//2],-A):
		R=b()
		if R>=E:return E
		if R>a:a=R
		if M>8:return a
		for F in W():
			if not F[3]&1 and not F[2]:continue
			f=B[F[1]]or-A
			if R+U[L(f)]+300<a:continue
			S=J(F)
			if K(H[(1+A)//2],A):N(S);continue
			D=-X(-E,-a,0,M+1);N(S)
			if D>=E:return E
			if D>a:a=D
		return a
	if d<=0:d=1
	G=P.get(C);Y=0
	if G:
		if G[0]>=d:
			D=G[2]
			if not G[1]or(D>=E if G[1]>0 else D<=a):return D
		Y=G[3]
	T=Z()
	if not T:return M-O if K(H[(1-A)//2],-A)else 0
	g=a;T.sort(key=lambda m:-(m==Y)*1000-U[L(B[m[1]])]);I=-O;e=T[0]
	for(h,F)in Q(T):
		S=J(F);D=-X(-E,-a,d-1-(h>2 and F[3]%2==0),M+1);N(S)
		if D>I:I=D;e=F
		a=max(a,D)
		if a>=E:break
	if P.get(C,(0,))[0]<=d:P[C]=d,(I>=E)-(I<=g),I,e
	return I
def m():
	V[0]=0;B=Z();A=B[0]
	for H in E(1,7):
		C=-O;D=A
		try:
			for F in B:
				I=J(F);G=-X(-O,-C,H-1,1);N(I)
				if G>C:C=G;D=F
			A=D;B.remove(A);B.insert(0,A)
		except c:break
	return A
def n(m):return chr(97+m[0]%8)+str((m[0]>>4)+1)+chr(97+m[1]%8)+str((m[1]>>4)+1)+(m[2]and'nbrq'[m[2]-2]or'')
def o(s):
	B=M(s[0])-97+(int(s[1])-1)*16;C=M(s[2])-97+(int(s[3])-1)*16;D=5-'qrbn'.index(s[4])if s[4:]else 0
	for A in W():
		if A[0]==B and A[1]==C and A[2]==D:return A
def p():
	D='game';C='status';E=os.environ['MAKEFUN_ENV_URL']
	def B(p,d):return I.load(e.urlopen(E+p,data=I.dumps(d).encode()))
	while 1:
		A=B('/game',{})
		if A[C]=='done':break
		P.clear()
		while A[C]=='your_move':l();[J(o(A))for A in A['moves']];F=m();A=B('/move',{D:A[D],'move':n(F)})
p()