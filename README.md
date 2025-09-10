# <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/b053eabc-0f70-4dd3-a5e7-ebe586e15bf0" /> DNA Global Alignment CLI Tool

## 🗒️ Project Overview
This project is a command-line tool for performing global alignment of DNA sequences using the Needleman-Wunsch algorithm. It allows users to:  

- Load DNA sequences from FASTA files or manual input  
- Perform global alignment between two sequences  
- Calculate matches, mismatches, gaps, and identity percentage 
- Visualize the alignment in the terminal (CLI)

[GIF]

## 🔑 Key Features
- FASTA file input: Supports standard DNA sequence files  
- Global alignment: Implements Needleman-Wunsch algorithm for full-sequence comparison  
- Scoring system: Match, mismatch, and gap penalties  
- Alignment statistics:
  - Number of matches  
  - Number of mismatches  
  - Number of gaps  
  - % identity between sequences  
- Optional visualization: Color-highlight mismatches and gaps in terminal  
- Extensible: Can later be adapted for RNA or protein sequences  

## 👾 Needleman-Wunsch Algorithm

The Needleman–Wunsch algorithm is a fundamental method in bioinformatics used to align protein or nucleotide sequences. Developed in 1970, it was one of the first applications of dynamic programming to biological sequence comparison.

The algorithm works by breaking a large problem (aligning full sequences) into smaller subproblems, then combining their solutions to find the optimal global alignment. Each possible alignment is assigned a score, and the algorithm identifies alignments with the highest possible score. Needleman–Wunsch algorithm is widely used when the quality of a global alignment is critical.

## 💻 How to use

1. Clone the repository:  
```bash
git clone https://github.com/<your_username>/dna-global-align.git
cd dna-global-align
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the program:
```bash
python src/main.py
```

4. Input paths to two FASTA files when prompted.

## 📚 References

- Needleman, S.B., & Wunsch, C.D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins.
- Mount, D.W. (2004). Bioinformatics: Sequence and Genome Analysis. Cold Spring Harbor Laboratory Press.
- EMBOSS Needle tool: https://www.ebi.ac.uk/jdispatcher/psa/emboss_needle
- Biopython Documentation: https://biopython.org/wiki/Documentation
