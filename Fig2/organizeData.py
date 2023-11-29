import pandas as pd

def reNameTE(TE_data):
	f=pd.read_table(TE_data,comment="#")
	f["Geneid"]=f["Geneid"].apply(lambda x: "TEcon_"+x)
	f["Chr"]=f["Chr"].apply(lambda x: "TEcon_"+x)
	return f

#te1=reNameTE("Fly_sh-white_RNA-seq.fastq_TE_full.fa.bam.TE.count.txt")
#te2=reNameTE("Fly_sh-aub_white_RNA-seq.fastq_TE_full.fa.bam.TE.count.txt")

def combineData(geneData,TE_data,name):
	f=pd.read_table(geneData,comment="#")
	columns=list(f.columns)[:-1]+[name]
	f.columns=columns
	TE_data.columns=columns
	all_data=f.append(TE_data,ignore_index=True)
	return all_data

#d1=combineData("Fly_sh-white_RNA-seq.fastq_dm6.fa.bam.Gene.count.txt",te1,"C")
#d2=combineData("Fly_sh-aub_white_RNA-seq.fastq_dm6.fa.bam.Gene.count.txt",te2,"T")

#d=d1.merge(d2,on=["Geneid","Chr","Start","End","Strand","Length"],how="inner")
#d.to_csv("white_aub_RNAseq.tsv",index=None,sep="\t")
#print(d[0:10])
#print(d.shape)

df=[]
dic={"Fly_sh-white_RNA-seq_pseudo_replicate":"C","Fly_sh-aub_white_RNA-seq_pseudo_replicate":"T"}
for n in ["Fly_sh-white_RNA-seq_pseudo_replicate","Fly_sh-aub_white_RNA-seq_pseudo_replicate"]:
	for i in [1,2,3]:
		te1=reNameTE("%s_%s.fastq_TE_full.fa.bam.TE.count.txt"%(n,i))
	#te2=reNameTE("Fly_sh-aub_white_RNA-seq_pseudo_replicate_%s.fastq_TE_full.fa.bam.TE.count.txt"%(i))
		d1=combineData("%s_%s.fastq_dm6.fa.bam.Gene.count.txt"%(n,i),te1,"%s_%s"%(dic[n],i))
	#d2=combineData("Fly_sh-aub_white_RNA-seq_pseudo_replicate_%s.fastq_dm6.fa.bam.Gene.count.txt"%(i),te2,"T_%s"%(i))
		df.append(d1)
	#df.append(d2)

f=pd.merge(df[0],df[1],on=["Geneid","Chr","Start","End","Strand","Length"],how="inner")
for df_ in df[2:]:
	f=pd.merge(f,df_,on=["Geneid","Chr","Start","End","Strand","Length"],how="inner")
print(f[0:10])
print(f.shape)
f.to_csv("white_aub_RNAseq.tsv",index=None,sep="\t")
