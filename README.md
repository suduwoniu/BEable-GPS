# BEable-GPS
Codes for gRNA design for a chosen cytosine base editors (BEs)

## Usage for nCas9-based BEs  
```
python BEable_Cas9_CtoT.py input_seq.txt PAM_sequence length_gRNA_spacer editing_window_start editing_window_end > result.txt
```

Example:  

```
python BEable_Cas9_CtoT.py seq.txt NGG 4 8 > BE3_results.txt
```

###### Parameters:  

***input_seq.txt:*** a file containing pathogenic SNV flanking sequences for gRNA design.  A seuqence in one line is of 61 nucleotides (A,T,C,G) and the 31st nucleotide of each sequence is the pathogenic SNV 						(C/G) for gRNA design .  
A example of input_seq.txt:  
TTTGATTTGGTGTGCCGGACTCTGGGGCTC**C**GAGAAACCTGGTTCTTTGGACTGCAGTACA  
AATTTATCTTCTTTTGGCTTCTCAGGAATC**C**ATACCTGTTTTGTATGTAAGCAGAGTGGGG  
GAGAAATATGAAGTCTTCATGGATGTTTGC**C**AAAATTTTCAACCAGTTTTCCGTTACTTCT  
GACCTGTCCCAGATGCTGAAGAAGATGCCT**C**AGTACCAGAAAGAGCTCAGCAAGGTATGGC  
TGTGTGCCATCGCTGGTGTGCTAACAATTG**C**CCTGCCCGTACCTGTCATTGTGTCCAATTT  

***PAM_sequence:*** PAM sequence of a chosen BE. For example, "NGG" for BE3, "NG" for xBE3.  
***length_gRNA_spacer:*** the length of gRNA spacer of a chosen BE. For example, 20 for BE3.  
***editing_window_start:*** the start position of editing window of a chosen BE.  
***editing_window_end:*** the end position of editing window of a chosen BE.  

Note: The start and end position of editing window is counted distally from PAM sequence. For example, spacer and PAM sequence of BE3: N<sub>1</sub>N<sub>2</sub>N<sub>3</sub><font color=#0099ff >N<sub>4</sub>N<sub>5</sub>N<sub>6</sub>N<sub>7</sub>N<sub>8</sub></font>N<sub>9</sub>N<sub>10</sub>N<sub>11</sub>N<sub>12</sub>N<sub>13</sub>N<sub>14</sub>N<sub>15</sub>N<sub>16</sub>N<sub>17</sub>N<sub>18</sub>N<sub>19</sub>N<sub>20</sub><font color=red >NGG</font>*, N1-20 is the spacer sequence, "*<font color=red>NGG</font>" is PAM sequence,N4-8 is the editing window of BE3, thus the start position of editing window is 4, and the end position of editing window is 8,

## Usage for Cpf1-based BEs    
```
python BEable_Cpf1_CtoT.py input_seq.txt PAM_sequence length_gRNA_spacer editing_window_start editing_window_end > result.txt 
```

Example:  

```
python BEable_Cpf1_CtoT.py seq.txt TTTV 23 8 13 > dCpf1-BE_result.txt 
```



Parameters are same to Cas9-based BEs mentioned above, and the only difference is the count of editing window position which is proximal from the PAM sequence.  
 For example, the PAM and spacer sequence for dCpf1-BE: <font color=red >TTTV</font>N<sub>1</sub>N<sub>2</sub>N<sub>3</sub>N<sub>4</sub>N<sub>5</sub>N<sub>6</sub>N<sub>7</sub><font color=#0099ff >N<sub>8</sub>N<sub>9</sub>N<sub>10</sub>N<sub>11</sub>N<sub>12</sub>N<sub>13</sub></font>N<sub>14</sub>N<sub>15</sub>N<sub>16</sub>N<sub>17</sub>N<sub>18</sub>N<sub>19</sub>N<sub>20</sub>N<sub>21</sub>N<sub>22</sub>N<sub>23</sub>, "<font color=red>TTTV</font>" is PAM sequence, N8-13 is the editing window, thus the start position of editing window is 8 and the end position of editing window is 13.

## Usage for nCas9-based BEs with special TC preference  

 This commond is specially used for eA3A-BE3 and BE3-R33A/K34A which have a preference for "TC" context.

```
python BEable_Cas9_CtoT_TCpreference.py input_seq.txt PAM_sequence length_gRNA_spacer editing_window_start editing_window_end > result.txt
```

Example:  

```
python BEable_Cas9_CtoT_TCpreference.py seq.txt NGG 20 4 8 > eA3A-BE3.txt
```

  

## Usage for searching all targetable sites in one sequence  
```
python BEable_search_sequence.py one_seuqence.txt PAM_sequence length_gRNA_spacer editing_window_start editing_window_end choose_BE_type > result.txt 
```


Example:
```
python BEable_search_sequence.py one_sequence.txt NGG 20 4 8 Cas9 > BE3_result.txt  
```

###### Parameters:

***one_sequence.txt:*** a plain txt file containing only one gene sequence (A, T, C, G). For example: "TTTGATTTGGTGTGCCGGACTCTGGGGCTCCGAGAAACCTGGTTCTTTGGACTGCAGTACAAATTTATCTTCTTTTGGCTTCTCAGGAATCCATACCTGTTTTGTATGTAAGCAGAGTGGGG"

***Choose_BE_type:*** "Cas9" or "Cpf1". Chosse which type of BEs are used. "Cas9" is for Cas9-based BEs, of which the position of editing window is counted distal from PAM sequence (N<sub>1</sub>N<sub>2</sub>N<sub>3</sub><font color=#0099ff >N<sub>4</sub>N<sub>5</sub>N<sub>6</sub>N<sub>7</sub>N<sub>8</sub></font>N<sub>9</sub>N<sub>10</sub>N<sub>11</sub>N<sub>12</sub>N<sub>13</sub>N<sub>14</sub>N<sub>15</sub>N<sub>16</sub>N<sub>17</sub>N<sub>18</sub>N<sub>19</sub>N<sub>20</sub><font color=red >NGG</font>). "Cpf1" is for Cpf1-based BEs, of which the position of editing window is counted proximal from the PAM sequence (<font color=red >TTTV</font>N<sub>1</sub>N<sub>2</sub>N<sub>3</sub>N<sub>4</sub>N<sub>5</sub>N<sub>6</sub>N<sub>7</sub><font color=#0099ff >N<sub>8</sub>N<sub>9</sub>N<sub>10</sub>N<sub>11</sub>N<sub>12</sub>N<sub>13</sub></font>N<sub>14</sub>N<sub>15</sub>N<sub>16</sub>N<sub>17</sub>N<sub>18</sub>N<sub>19</sub>N<sub>20</sub>N<sub>21</sub>N<sub>22</sub>N<sub>23</sub>).



The web version of these tools are avaliable at: [http://www.picb.ac.cn/rnomics/BEable-GPS/](http://www.picb.ac.cn/rnomics/BEable-GPS/) 

