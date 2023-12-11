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
args=parser.parse_args()

reference=args.RefSeq
out=args.Outname
TEseq=list(SeqIO.parse(reference,"fasta"))
sequence=str(TEseq[0].seq)
ID=TEseq[0].id


def simulate(fron,end,start,top,copy,direction,LTR,len_LTR):
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
	template=Seq(sequence[front:end])
	first=Seq(sequence[front:start])
	second=Seq(sequence[stop:end])
	if direction=="+":
		return str(second)+ str(template)*copty +str(first)
	if direction=="-":
		return str(first.reverse_complement())+str(template.reverse_complement())*copy+str(second.reverse_complement())
	

def generateFile(filename,start,end,nSeq):
	f=open(filename,"w")
	for i in range(0,nSeq):
		middle=random.randint(start,end)
		copy=random.randint(0,11)
		stop=random.randint(start,end)
		direction=random.choice(["+","-"])
		parameter=[start,end,middle,copy,stop,direction]
		parameter=[str(c) for c in parameter]
		name=filename+str(i+1)+"_"+"_".join(parameter)
		read=Simulate(start,end,middle,copy,stop,direction)
		f.write(">"+name+"\n"+read+"\n")

def FalsePostive(filename,nSeq):
	f=open(filename,"w")
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
		name=filename+str(i+1)+"_"+"_".join(parameter)
		f.write(">"+name+"\n"+amplify+"\n")

generateFile(out+"_full.fa",0,len(sequence),1)
r1=random.randint(0,len(sequence))
r2=random.randint(0,len(sequence))
generateFile(out+"_frag.fa",min((r1,r2)),max((r1,r2)),1)
FalsePostive(out+"_FP.fa",1)
