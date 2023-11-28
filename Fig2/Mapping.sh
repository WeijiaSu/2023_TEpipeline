#!/bin/bash

## Modify this job script accordingly and submit with the command:
##    sbatch HPC.sbatch

#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=16   # 16 processor core(s) per node
#SBATCH --job-name='Mapping'
#SBATCH --output="Mapping-%j.out"
#SBATCH --error="Mapping-%j.err"
#SBATCH --partition="all"
#SBATCH --mail-user=weijia.su@duke.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mem=100000
## LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE


module load samtools
HMS="/data/zhanglab/Weijia_Su/CommonDataSet/TE_full/HMS-Beagle.fasta"
TE="/data/zhanglab/Weijia_Su/CommonDataSet/TE_full.fa"
genome="/data/zhanglab/Weijia_Su/Genomes/Dro/dm6.fa"

Datapath="/data/zhanglab/Weijia_Su/Nanopore_Raw_Data/210914-fly-vasKD-ovary-RNA/"

for fileName in Fly_sh-aub_white_RNA-seq Fly_sh-white_RNA-seq;
do
for sub in {1..3};
do
reads=$Datapath$fileName"_pseudo_replicate_"$sub".fastq";
name=$(basename $reads)
for ref in $HMS $TE $genome;
do
refName=$(basename $ref);
echo $name"_"$refName;
minimap2 -ax splice $ref $reads -Y -t 16 | samtools view -bS | samtools sort > $name"_"$refName".bam";
samtools index $name"_"$refName".bam";
samtools stats $name"_"$refName".bam" | head -n 30  > $name"_"$refName".bam.stat";
done
done
done

GenomeRef="/data/zhanglab/Weijia_Su/Genomes/Dro/dm6.ncbiRefSeq.gtf"
TERef="/data/zhanglab/Weijia_Su/Genomes/Dro/Flybase_transposon_sequence_set.fa.saf"
for i in *dm6.fa*.bam;
do
featureCounts -L -O -M --fraction -F GTF -s 0 -a $GenomeRef -o $i".Gene.count.txt" $i;
done

for i in *TE_full.fa*.bam;
do
featureCounts -L -O -M --fraction -F SAF -s 0 -a $TERef -o $i".TE.count.txt" $i;
done
