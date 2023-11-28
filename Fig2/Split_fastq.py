from Bio import SeqIO
import random

def split_fastq(file_path,out_name,num_splits=3):
    # Read sequences from the FASTQ file
    sequences = list(SeqIO.parse(file_path, "fastq"))

    # Shuffle the sequences to ensure randomness
    random.shuffle(sequences)

    # Split sequences into `num_splits` parts
    splits = [[] for _ in range(num_splits)]
    for i, sequence in enumerate(sequences):
        splits[i % num_splits].append(sequence)

    # Write each part to a new file
    for i, split in enumerate(splits):
        with open( out_name+f"_pseudo_replicate_{i+1}.fastq", "w") as output_handle:
            SeqIO.write(split, output_handle, "fastq")


# Replace 'your_fastq_file.fastq' with the path to your FASTQ file
split_fastq('/data/zhanglab/Weijia_Su/Nanopore_Raw_Data/210914-fly-vasKD-ovary-RNA/Fly_sh-aub_white_RNA-seq.fastq',"Fly_sh-aub_white_RNA-seq")
split_fastq('/data/zhanglab/Weijia_Su/Nanopore_Raw_Data/210914-fly-vasKD-ovary-RNA/Fly_sh-white_RNA-seq.fastq',"Fly_sh-white_RNA-seq.fastq")

