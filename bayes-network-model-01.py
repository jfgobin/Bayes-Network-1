import random

def eventA():
	n=random.randint(0,99)
	if n < 45:
		return True
	return False

def eventB(A):
	n=random.randint(0,99)
	if A:
		if n < 15:
			return True
	else:
		if n < 95:
			return True
	return False

def eventC(A):
	n=random.randint(0,99)
	if A:
		if n < 85:
			return True
	else:
		if n < 45:
			return True
	return False

def eventD(A,B):
	n=random.randint(0,99)
	if A and B and n < 95:
		return True
	if A and not B and n < 75:
		return True
	if not A and B and n < 55:
		return True
	if not A and not B and n < 35:
		return True
	return False

PB=0.0
PC=0.0
PBC=0.0
PD=0.0
PBD=0.0
PCD=0.0
PBCD=0.0
PA=0.0
PBA=0.0
PCA=0.0
PBCA=0.0

PAD=0.0
PBAD=0.0
PCAD=0.0
PBCAD=0.0

for j in range(0,1000000):
	A=eventA()
	B=eventB(A)
	C=eventC(A)
	D=eventD(B,C)
	if B:
		PB+=1.0
	if C:
		PC+=1.0
	if B and C:
		PBC+=1.0
	if D:
		PD+=1.0
		if B:
			PBD+=1.0
		if C:
			PCD+=1.0
		if B and C:
			PBCD+=1.0
	if not A:
		PA+=1.0
		if B:
			PBA+=1.0
		if C:
			PCA+=1.0
		if B and C:
			PBCA+=1.0
	if not A and not D:
		PAD+=1.0
		if B:
			PBAD+=1.0
		if C:
			PCAD+=1.0
		if B and C:
			PBCAD+=1.0

K=1000000.0
print "P(B)=        ", PB/K
print "P(B|C)=      ", PBC/PC
print "P(C)=        ", PC/K
print "P(C|B)=      ", PBC/PB
print " "
print "P(C,(D))=    ", PCD/PD
print "P(C|B,(D))=  ", PBCD/PBD
print "P(B,(D))=    ", PBD/PD
print "P(B|C,(D))=  ", PBCD/PCD
print " "
print "P(C,(A))=    ", PCA/PA
print "P(C|B,(A))=  ", PBCA/PBA
print "P(B,(A))=    ", PBA/PA
print "P(B|C,(A))=  ", PBCA/PCA
print " "
print "P(C,(A,D))=  ", PCAD/PAD
print "P(C|B,(A,D))=", PBCAD/PBAD
print "P(B,(A,D))=  ", PBAD/PAD
print "P(B|C,(A,D))=", PBCAD/PCAD
