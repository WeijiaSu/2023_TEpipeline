from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import random
import sys
import os

random.seed(42)

def load_fasta(file_path,chromosome=None):
    genomefile=list(SeqIO.parse(file_path, "fasta"))
    if chromosome != None:
        genomefile=[i for i in genomefile if i.id in chromosome]
    return genomefile

def save_fasta(sequences, file_path):
    SeqIO.write(sequences, file_path, "fasta")

def simulate_insertion(genome, transposon, insertion_points):
    for point in insertion_points:
        genome.seq = genome.seq[:point] + transposon.seq + genome.seq[point:]
    return genome

def select_genome(genome):
    genome_seq = random.choice(genome)
    random_point=random.randint(0, len(genome_seq.seq)-100000)
    random_lengh=random.randint(100,100000)
    #print("selected: %s(%s): %s - %s"%(genome_seq.id,len(genome_seq.seq),random_point,random_point+random_lengh))
    random_seq=genome_seq.seq[random_point:random_point+random_lengh]
    return [genome_seq.id,random_point,random_point+random_lengh,random_seq]

fly = ["chr2L", "chr2R", "chr3L", "chr3R", "chr4"]
def main():
    # Load genome and transposon sequences
    genome_file = sys.argv[1]
    transposon_file = sys.argv[2]
    
    genome_sequences = load_fasta(genome_file,fly)
    print("Reading genome file...")
    transposon_sequences = load_fasta(transposon_file)
    print("Reading transposon file...")
    # List to hold modified genome sequences
	
    modified_genome_sequences = []
    
    # Simulate 100 insertions for each transposon in different genome sequences
    for transposon in transposon_sequences:
        for _ in range(100):  # 100 insertions per transposon
            # Choose a random genome sequence for each insertion
            print("Simulating %s #%s "%(transposon.id,_+1))
            genome=select_genome(genome_sequences)
            genome_seq=genome[-1]
			# Choose a random insertion point within the genome sequence
            insertion_point = random.randint(0, len(genome_seq))
            # Simulate insertion
            genome_seq = genome_seq[:insertion_point] + transposon.seq + genome_seq[insertion_point:]
            genome_id="_".join([str(i) for i in genome[0:3]]+[transposon.id,str(insertion_point)])
            seq_record = SeqRecord(genome_seq, id=genome_id, description="")
            modified_genome_sequences.append(seq_record)

    output_file = sys.argv[3]
    save_fasta(modified_genome_sequences, output_file)

if __name__ == "__main__":
    main()

