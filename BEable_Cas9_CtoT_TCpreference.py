import regex
import re
import sys
import readFile
file=sys.argv[1]
PAM=sys.argv[2]
spacerLen=int(sys.argv[3])
windowstart=int(sys.argv[4])
windowend=int(sys.argv[5])

#seqLen=len(seq)
pamLen=len(PAM)
#enc_pam=create_PAM(PAM)
windowlen=windowend-windowstart+1

def RC(seq):
    encoder = {'A':'T','T':'A','C':'G','G':'C','N':'N','R':'Y','Y':'R', 'M':'K', 'K':'M', 'S':'S', 'W':'W', 'H':'D', 'B':'V', 'V':'B', 'D':'H'}
    rc = ''
    for n in reversed(seq):
        rc += encoder[n]
    return rc
def create_PAM(pam):
    encoder = {'A':'A','T':'T','G':'G','C':'C','R':'[A|G]','Y':'[C|T]','N':'[A|T|C|G]','M':'[A|C]','K':'[G|T]','S':'[C|G]','W':'[A|T]','H':'[A|C|T]','B':'[C|G|T]','V':'[A|C|G]','D':'[A|G|T]'}
    enc_pam = {'f':'','r':''}
    rc_pam = RC(pam)
    for n,m in zip(pam, rc_pam):
        enc_pam['f'] += encoder[n]
        enc_pam['r'] += encoder[m]
    return enc_pam
enc_pam=create_PAM(PAM)
ref=readFile.readFile(file)
results=[]
for n in range(len(ref)):
    seq=ref[n][0]
    gRNA=[]
    if seq[30]=="C":
	pc=seq[29:31]
	if pc=="TC":
	    L=list(seq)
	    L[30]="Y"
	    #seq[30]="Y"
	    seq=''.join(L)
	    for i in range(windowstart-1,windowend):
	        pStart=30+spacerLen-i
                if regex.match(enc_pam['f'],seq[pStart:pStart+pamLen]):
		    gRNA.append(seq[30-i:30-i+pamLen+spacerLen])
    if seq[30]=="G":
	pc=seq[30:32]
	if pc=="GA":
            L=list(seq)
	    L[30]="R"
	#seq[30]="R"
	    seq=''.join(L)
            for i in range(windowstart-1,windowend):
	        pStart=30-spacerLen+i-pamLen+1
	        if regex.match(enc_pam['r'],seq[pStart:pStart+pamLen]):
		    gRNA.append(seq[pStart:pStart+pamLen+spacerLen])
    results.append(gRNA)

for i in range(len(ref)):
    if len(results[i]):
	print ','.join(results[i])
    else:
	print 'none'
