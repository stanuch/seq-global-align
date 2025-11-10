from Bio import SeqIO

def read_fasta(file_path):
    for record in SeqIO.parse(file_path, "fasta"):
        return str(record.seq)