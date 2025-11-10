import os
from fasta_read import read_fasta
from needle import needleman_wunsch
from Bio import SeqIO

def get_file_path(base_dir, filename):
    seq_dir = os.path.join(base_dir, "..", "sequences") # fasta files path
    return os.path.join(seq_dir, f"{filename}.fasta")

def print_sequences(file_path, label):
    print(f"{label}:")
    for record in SeqIO.parse(file_path, "fasta"):
        print(f"ID: {record.id}")
        print(f"Seqence: {record.seq}\n")

def similarity_percentage(seq1, seq2):
    if len(seq1) >= len(seq2):
        long_seq = seq1
        short_seq = seq2
    else:
        long_seq = seq2
        short_seq = seq1

    min_length = len(short_seq)
    max_length = len(long_seq)
    max_similarity_count = 0

    if min_length == 0:
        return 0.0

    for i in range(max_length - min_length + 1):
        current_similarity_count = 0
        for j in range(min_length):
            if short_seq[j] == long_seq[i + j]:
                current_similarity_count += 1
        if current_similarity_count > max_similarity_count:
            max_similarity_count = current_similarity_count

    percentage = (max_similarity_count / min_length) * 100

    return percentage
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    cls()
    base_dir = os.path.dirname(os.path.abspath(__file__)) # main.py path

    seq1_filename = input("Enter the name of sequence 1 file (without extension): ")
    seq2_filename = input("Enter the name of sequence 2 file (without extension): ")
    print("")

    seq1_path = get_file_path(base_dir, seq1_filename)
    seq2_path = get_file_path(base_dir, seq2_filename)

    sequence1 = read_fasta(seq1_path)
    sequence2 = read_fasta(seq2_path)

    sequences = []
    sequences.append(read_fasta(seq1_path))
    sequences.append(read_fasta(seq2_path))

    aligned1, aligned2, score = needleman_wunsch(sequences[0], sequences[1], matrix_name="BLOSUM62", gap_open=-10, gap_extend=-0.5)

    print("\nAlignment:")
    print(aligned1)
    print(aligned2)
    print(f"\nAlignment score: {score}")


    print
    similar = similarity_percentage(sequence1, sequence2)
    print(f"Similarity: {similar:.2f}%\n")

if __name__ == "__main__":
    main()
