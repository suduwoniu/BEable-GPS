# BEable-GPS
Codes for gRNA design for a chosen cytosine base editors (BEs)

## Usage for nCas9-based BEs  
python BEable_Cas9_CtoT.py input_seq.txt PAM_sequence length_gRNA_spacer ED_start ED_end > result.txt

Example:  
python BEable_Cas9_CtoT.py seq.txt NGG 4 8 > BE3_results.txt

Parameters:  
input_seq.txt: a file containing all sequences for gRNA design, and a seuqence is of 61 nucleotides (A,T,C,G) in one line in this file. The 31st nucleotide of each sequence is C/G for BEs targeting.  
A example of input_seq.txt:  
TTTGATTTGGTGTGCCGGACTCTGGGGCTCCGAGAAACCTGGTTCTTTGGACTGCAGTACA  
AATTTATCTTCTTTTGGCTTCTCAGGAATCCATACCTGTTTTGTATGTAAGCAGAGTGGGG  
GAGAAATATGAAGTCTTCATGGATGTTTGCCAAAATTTTCAACCAGTTTTCCGTTACTTCT  
GACCTGTCCCAGATGCTGAAGAAGATGCCTCAGTACCAGAAAGAGCTCAGCAAGGTATGGC  
TGTGTGCCATCGCTGGTGTGCTAACAATTGCCCTGCCCGTACCTGTCATTGTGTCCAATTT  
AAAGGAGCTCCAAGGAGAGGACAGAAAACACGAAGGAAAAACACCTCTGCTCACTTTCTTC  

PAM_sequence: PAM sequence of a chosen BE. For example, "NGG" for BE3, "NG" for xBE3.  
length_gRNA_spacer: the length of gRNA spacer of a chosen BE. For example, 20 for BE3.  
ED_start: the start position of editing window of a chosen BE.  
ED_end: the end position of editing window of a chosen BE.  
(Note: count of editing window position is distal from PAM. For example, N1N2N3N4N5N6N7N8N9N10N11N12N13N14N15N16N17N18N19N20NGG, "NGG" is PAM sequence, the start position of editing window is 4, and the end position of editing window is 8),
  
## Usage for Cpf1-based BEs    
python BEable_Cpf1_CtoT.py input_seq.txt PAM_sequence length_gRNA_spacer ED_start ED_end > result.txt 

Example:  
python BEable_Cpf1_CtoT.py seq.txt TTTV 23 8 13 > dCpf1-BE_result.txt  

Parameters are same to Cas9-based BEs mentioned above, only one difference is the editing window position which is proximal from the PAM sequence.  
 For example, TTTVN1N2N3N4N5N6N7N8N9N10N11N12N13N14N15N16N17N18N19N20N21N22N23, "TTTV" is PAM sequence, the start position of editing window is 8 and the end position of editing window is 13.

## Usage for nCas9-based BEs with specially TC preference  
python BEable_Cas9_CtoT_TCpreference.py input_seq.txt PAM_sequence length_gRNA_spacer ED_start ED_end > result.txt

Example:  
python BEable_Cas9_CtoT_TCpreference.py seq.txt NGG 20 4 8 > eA3A-BE3.txt  

## Usage for searching all targetable sites in one sequence  
python BEable_search_sequence.py one_seuqence.txt PAM_sequence length_gRNA_spacer ED_start ED_end > result.txt  
Example:
python BEable_search_sequence.py one_sequence.txt NGG 20 4 8 > result.txt  

one_sequence.txt: one gene sequence for BE targeting
