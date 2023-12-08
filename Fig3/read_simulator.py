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


def Simulate_1LTR_FL(start,stop,copy,direction,len_LTR):
	front=0
	end=len(sequence)-len_LTR
	template=sequence[front:end]
	first=Seq(sequence[1:start])
	second=Seq(sequence[stop:len(sequence)-len_LTR])
	if direction=="+":
		return str(second)+ template*copty +str(first)
	if direction=="-":
		
	

def Simulate(start,end,middle,copy,stop,direction):
	first=Seq(sequence[start:middle])
	second=Seq(sequence[middle:end])
	if direction=="+":
		template=str(second)+str(first)
	else:
		first=str(first.reverse_complement())
		second=str(second.reverse_complement())
		template=first+second
	if copy==0 and direction=="+":
		stop1=random.randint(0,len(str(first)))
		return str(second)+str(first)[:stop1]
	elif copy==0 and direction=="-":
		stop1=random.randint(0,len(str(second)))
		return str(Seq(sequence[start:middle]).reverse_complement())+str(Seq(sequence[middle:end]).reverse_complement())[0:stop1]
	else:
		amplify=template*copy
		last=template[:stop]
		return amplify+last


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
