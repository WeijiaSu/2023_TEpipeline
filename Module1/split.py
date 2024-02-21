import random

def read_fastq(file_path):
    with open(file_path, 'r') as fastq_file:
        lines = fastq_file.readlines()
        
    # Group every four lines into a single read
    reads = [lines[i:i+4] for i in range(0, len(lines), 4)]
    return reads

def write_fastq(reads, output_path):
    with open(output_path, 'w') as outfile:
        for read in reads:
            outfile.writelines(read)

def split_fastq(file_path, output_path1, output_path2):
    reads = read_fastq(file_path)
    
    # Shuffle reads to randomize
    random.shuffle(reads)
    
    # Split reads into two parts
    mid_point = len(reads) // 2
    part1 = reads[:mid_point]
    part2 = reads[mid_point:]
    
    # Write to output files
    write_fastq(part1, output_path1)
    write_fastq(part2, output_path2)

# Example usage
file_path = '/data/zhanglab/Weijia_Su/Nanopore_Raw_Data/210914-fly-vasKD-ovary-RNA/Fly_sh-white_RNA-seq.fastq'  # Change this to your FASTQ file path
output_path1 = 'Fly_sh-white_RNA-seq.fastq_1.fastq'  # Change this for the first output file
output_path2 = 'Fly_sh-white_RNA-seq.fastq_2.fastq'  # Change this for the second output file

split_fastq(file_path, output_path1, output_path2)

