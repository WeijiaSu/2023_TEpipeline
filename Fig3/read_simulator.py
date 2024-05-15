import pandas as pd
from Bio import SeqIO
import argparse
import os
import random
from Bio.Seq import Seq

pd.set_option("display.max_columns",40)


parser=argparse.ArgumentParser()

parser.add_argument("-Ref","--RefSeq")
parser.add_argument("-out","--Outname")
parser.add_argument("-nSeq","--NumberofSeq")
parser.add_argument("-len_LTR","--LTRlength")
parser.add_argument("-seed","--SEED",default=2)
args=parser.parse_args()

reference=args.RefSeq
out=args.Outname
TEseq=list(SeqIO.parse(reference,"fasta"))
sequence=str(TEseq[0].seq)
ID=TEseq[0].id
nSeq=args.NumberofSeq
nSeq=int(nSeq)
len_LTR=int(args.LTRlength)
random.seed(int(args.SEED))

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
		return parameter,str(second)+ str(template)*copy +str(first)
	if direction=="-":
		parameter=["LTR:"+str(LTR),front,end,start,stop,copy,direction]
		return parameter,str(first.reverse_complement())+str(template.reverse_complement())*copy+str(second.reverse_complement())
	

def generate_(seq,filename,nSeq):
	length=len(sequence)
	f=open(filename,"w")
	for LTR in [1,2,5,3,0]:
		for i in range(0,nSeq):
			front=random.randint(0,length)
			end=random.randint(front,length)
			copy=random.randint(0,11)
			direction=random.choice(["+","-"])
			parameters,read=simulate(front,end,copy,direction,LTR,len_LTR)
			parameters=[str(i) for i in parameters]
			name=ID+"_"+str(i+1)+"_"+"_".join(parameters)
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
		name=ID+"_"+str(i+1)+"_"+"FP_"+"_".join(parameter)
		f.write(">"+name+"\n"+amplify+"\n")
	f.close()

generate_(sequence,out,nSeq)
FalsePostive(out,nSeq)
