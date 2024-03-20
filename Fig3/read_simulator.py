import pandas as pd
from Bio import SeqIO
import argparse
import os
import random
from Bio.Seq import Seq

random.seed(2)
pd.set_option("display.max_columns",40)


parser=argparse.ArgumentParser()

parser.add_argument("-Ref","--RefSeq")
parser.add_argument("-out","--Outname")
parser.add_argument("-nSeq","--NumberofSeq")
parser.add_argument("-len_LTR","--LTRlength")
args=parser.parse_args()

reference=args.RefSeq
out=args.Outname
TEseq=list(SeqIO.parse(reference,"fasta"))
sequence=str(TEseq[0].seq)
ID=TEseq[0].id
nSeq=args.NumberofSeq
nSeq=int(nSeq)
len_LTR=args.LTRlength


def simulate(front,end,copy,direction,LTR,len_LTR):
	if LTR==1:
		front=0
		end=len(sequence)-len_LTR
	if LTR==2:
		front=0
		end=len(sequence)
	if LTR==5:
		front=0
	if LTR==3:
		end=len(sequence)
	start=random.randint(front,end)
	stop=random.randint(front,end)
	template=Seq(sequence[front:end])
	first=Seq(sequence[front:start])
	second=Seq(sequence[stop:end])
	if direction=="+":
		parameter=["LTR:"+str(LTR),front,end,start,stop,copy,direction]
		return parameter,str(second)+ str(template)*copty +str(first)
	if direction=="-":
		return parameter,str(first.reverse_complement())+str(template.reverse_complement())*copy+str(second.reverse_complement())
	

def generate_(seq,filename,nSeq):
	length=len(sequence)
	f=open(filename,"w")
	for i in range(0,nSeq):
		for ltr in [1,2,5,3,0]:
			for i in range(0,nSeq):
				front=random.randint(0,length)
				end=random.randint(front,length)
				copy=random.randint(0,11)
				direction=random.choice(["+","-"])
				parameter,read=Simulate(front,end,copy,direction,LTR,len_LTR)
				name=filename+"_"+str(i+1)+"_"+"_".join(parameter)
				f.write(">"+name+"\n"+read+"\n")
	f.close()

def FalsePostive(filename,nSeq):
	f=open(filename,"a")
	for i in range(0,nSeq):
		length=len(sequence)
		r1=random.randint(0,length)
		r2=random.randint(0,length)
		start=min(r1,r2)
		end=max(r1,r2)
		template=sequence[start:end]
		copy=random.randint(0,11)
		amplify=template*copy
		parameter=[start,end,copy]
		parameter=[str(c) for c in parameter]
		name=filename+"_"+str(i+1)+"_"+"FP_"+"_".join(parameter)
		f.write(">"+name+"\n"+amplify+"\n")
	f.close()

generate_(sequence,out,nSeq)
FalsePostive(out,nSeq)
