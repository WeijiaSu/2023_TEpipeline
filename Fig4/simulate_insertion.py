
import Bio import SeqIO
import random
import sys
import os

def load_fasta(file_path):
    return list(SeqIO.parse(file_path, "fasta"))

def save_fasta(sequences, file_path):
    SeqIO.write(sequences, file_path, "fasta")

def simulate_insertion(genome, transposon, insertion_points):
    for point in insertion_points:
        genome.seq = genome.seq[:point] + transposon.seq + genome.seq[point:]
    return genome

fly = ["chr2L", "chr2R", "chr3L", "chr3R", "chr4", "chrM"]

def select_genome:
	

def main():
    # Load genome and transposon sequences
    genome_file = sys.argv[1]
    transposon_file = sys.argv[2]
    
    genome_sequences = load_fasta(genome_file)
    transposon_sequences = load_fasta(transposon_file)
    
    # List to hold modified genome sequences
	
    modified_genome_sequences = []
    
    # Simulate 100 insertions for each transposon in different genome sequences
    for transposon in transposon_sequences:
        for _ in range(100):  # 100 insertions per transposon
            # Choose a random genome sequence for each insertion
            genome = random.choice(genome_sequences)
            # Choose a random insertion point within the genome sequence
            insertion_point = random.randint(0, len(genome.seq))
            # Simulate insertion
            modified_genome = simulate_insertion(genome, transposon, [insertion_point])
            modified_genome_sequences.append(modified_genome)
    
    # Save all modified genome sequences
    output_file = "modified_fly_genomes.fasta"
    save_fasta(modified_genome_sequences, output_file)
    print(f"Modified genomes saved to {output_file}")

if __name__ == "__main__":
    main()

