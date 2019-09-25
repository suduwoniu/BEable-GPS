import sys
import re
import regex
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

def Editable_search(seq,PAM,windowstart,windowend,spacerLen,cpf,TCprefer):
    sgRNA_all=[]
    seqLen=len(seq)
    pamLen=len(PAM)
    C_sgRNA={}
    G_sgRNA={}
    for i in range(seqLen):
        C_sgRNA[i]=[]
        G_sgRNA[i]=[]
        enc_pam=create_PAM(PAM)
        windowlen=windowend-windowstart+1
    if cpf==False:
        for i in range(spacerLen,(seqLen-pamLen+1)):
            if regex.match(enc_pam['f'],seq[i:i+pamLen]):
                windowseq=seq[(i-spacerLen+windowstart-1):(i-spacerLen+windowend)]
                for j in range(len(windowseq)):
                    if windowseq[j]=="C":
                        if TCprefer==False:
                            sgSeq=seq[i-spacerLen:i+pamLen]
                            s=list(sgSeq)
                            s[windowstart+j-1]="Y"
                            sgSeq=''.join(s)
                            C_sgRNA[i-spacerLen+windowstart-1+j].append(sgSeq)
                        else:
                            if i-spacerLen+windowstart-1+j-1>=0:
                                whetherT=seq[i-spacerLen+windowstart-1+j-1]
                                if whetherT=="T":
                                    sgSeq=seq[i-spacerLen:i+pamLen]
                                    s=list(sgSeq)
                                    s[windowstart+j-1]="Y"
                                    sgSeq=''.join(s)
                                    C_sgRNA[i-spacerLen+windowstart-1+j].append(sgSeq)
        for i in range(0,(seqLen-spacerLen)):
            if regex.match(enc_pam['r'],seq[i:i+pamLen]):
                windowseq=seq[(i+spacerLen+pamLen-windowend):(i+spacerLen+pamLen-windowstart+1)]
                for j in range(len(windowseq)):
                    if windowseq[j]=="G":
                        if TCprefer==False:
                            sgSeq=seq[i:i+spacerLen+pamLen]
                            s=list(sgSeq)
                            s[spacerLen+pamLen-windowend+j]="R"
                            sgSeq=''.join(s)
                            G_sgRNA[i+spacerLen+pamLen-windowend+j].append(sgSeq)
                        else:
                            if i+spacerLen+pamLen-windowend+j+1<seqLen:
                                whetherT=seq[i+spacerLen+pamLen-windowend+j+1]
                                if whetherT=="A":
                                    sgSeq=seq[i:i+spacerLen+pamLen]
                                    s=list(sgSeq)
                                    s[spacerLen+pamLen-windowend+j]="R"
                                    sgSeq=''.join(s)
                                    G_sgRNA[i+spacerLen+pamLen-windowend+j].append(sgSeq)
        for i in range(len(seq)):
            if len(C_sgRNA[i]):
                sgRNA_all.append(','.join(C_sgRNA[i]))
            else:
                if len(G_sgRNA[i]):
                    sgRNA_all.append(','.join(G_sgRNA[i]))
                else:
                    sgRNA_all.append('none')
    if cpf==True:
        for i in range(0,seqLen-pamLen-spacerLen+1):
            if regex.match(enc_pam['f'],seq[i:i+pamLen]):
                windowseq=seq[i+pamLen+windowstart-1:i+pamLen+windowend]
                for j in range(len(windowseq)):
                    if windowseq[j]=="C":
                        if TCprefer==False:
                            sgSeq=seq[i:i+pamLen+spacerLen]
                            s=list(sgSeq)
                            s[pamLen+windowstart+j-1]="Y"
                            sgSeq="".join(s)
                            C_sgRNA[i+pamLen+windowstart-1+j].append(sgSeq)
                        else:
                            if i+pamLen+windowstart-1+j-1>=0:
                                whetherT=seq[i+pamLen+windowstart-1+j-1]
                                if whetherT=="T":
                                    sgSeq=seq[i:i+pamLen+spacerLen]
                                    s=list(sgSeq)
                                    s[pamLen+windowstart+j-1]="Y"
                                    sgSeq="".join(s)
                                    C_sgRNA[i+pamLen+windowstart-1+j].append(sgSeq)
        for i in range(spacerLen,seqLen-pamLen+1):
            if regex.match(enc_pam['r'],seq[i+spacerLen:i+spacerLen+pamLen]):
                windowseq=seq[(i+spacerLen-windowend):(i+spacerLen-windowstart+1)]
                for j in range(len(windowseq)):
                    if windowseq[j]=="G":
                        if TCprefer==False:
                            sgSeq=seq[i:i+spacerLen+pamLen]
                            s=list(sgSeq)
                            s[spacerLen-windowend+j]="R"
                            sgSeq=''.join(s)
                            G_sgRNA[i+spacerLen-windowend+j].append(sgSeq)
                        else:
                            if i+spacerLen-windowend+j+1<seqLen:
                                whetherT=seq[i+spacerLen-windowend+j+1]
                                if whetherT=="A":
                                    sgSeq=seq[i:i+spacerLen+pamLen]
                                    s=list(sgSeq)
                                    s[spacerLen-windowend+j]="R"
                                    sgSeq=''.join(s)
                                    G_sgRNA[i+spacerLen-windowend+j].append(sgSeq)
        for i in range(len(seq)):
            if len(C_sgRNA[i]):
                sgRNA_all.append(','.join(C_sgRNA[i]))
            else:
                if len(G_sgRNA[i]):
                    sgRNA_all.append(','.join(G_sgRNA[i]))
                else:
                    sgRNA_all.append('none')
    return sgRNA_all
seq_file=sys.argv[1]
PAM=sys.argv[2]
spacerLen=int(sys.argv[3])
windowstart=int(sys.argv[4])
windowend=int(sys.argv[5])
fl=open(seq_file)
for line in fl:
    linelist=line.split('\n')
line=linelist[0].upper()
if sys.argv[6]=="Cas9":
    sgRNA=Editable_search(line,PAM,windowstart,windowend,spacerLen,True,False)
if sys.argv[6]=="Cpf1":
    sgRNA=Editable_search(line,PAM,windowstart,windowend,spacerLen,False,False)
print "Position","\t","C/G","\t","gRNA_target+PAM"
for i in range(len(line)):
    if sgRNA[i]!="none":
	print i+1,'\t',line[i],"\t",sgRNA[i]
