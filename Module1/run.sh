#!/bin/bash

## Modify this job script accordingly and submit with the command:
##    sbatch HPC.sbatch

#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=1   # 16 processor core(s) per node
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


python3 split.py
#python3 /data/zhanglab/Weijia_Su/2023_Pipeline/Script/Split_fastq.py
