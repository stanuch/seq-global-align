# <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/b053eabc-0f70-4dd3-a5e7-ebe586e15bf0" /> Sequence Global Alignment Tool

![License](https://img.shields.io/badge/License-MIT-green) 
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=Python) 
![Status](https://img.shields.io/badge/status-functional-success)
![Stage](https://img.shields.io/badge/stage-proof_of_concept-orange)
![Last Commit](https://img.shields.io/github/last-commit/stanuch/seq-global-align)

## Project Overview
This project is a command-line tool for performing global alignment of DNA or protein sequences using the Needleman-Wunsch algorithm. It allows users to:  

- Load sequences using FASTA format
- Perform global alignment between two sequences
- Read and display info included in FASTA files

## Key Features
- FASTA file input: Supports standard DNA/protein sequence files  
- Global alignment: Implements simplified Needleman-Wunsch algorithm for full-sequence comparison
- Similarity: Calculates a similarity percentage score based on the optimal alignment of two sequences
- Scoring system: Match, mismatch, and gap penalties, substitution matrix (BLOSUM62) 

## Needleman-Wunsch Algorithm

The algorithm works by dividing the global alignment problem into smaller subproblems. It uses a scoring system that assigns values for matches, mismatches, and gaps. Then, it systematically fills a matrix where each cell represents the best score achievable for aligning the sequences up to that point. After filling the matrix, the algorithm traces back from the last cell to the first to determine the optimal alignment.

The simplified version focuses on the core concepts:
- Initialization of the scoring matrix with gap penalties.
- Matrix filling using a basic scoring scheme for matches, mismatches, and gaps.
- Traceback to reconstruct one optimal alignment, without considering multiple equally optimal solutions.

This simplified approach retains the main idea of finding a global alignment while being easier to understand and implement, making it ideal for educational purposes or quick sequence comparisons.

## How to use

1. Clone the repository:  
```bash
git clone https://github.com/stanuch/seq-global-align.git
cd dna-global-align
```

2. Install dependencies
- Make sure you have Python 3 installed, then run:
```bash
pip install -r requirements.txt
```

3. Prepare your FASTA files

- Place your sequence files in the sequences/ folder (already included in the repo).
- Use the .fasta format.
- When running the program, enter only the file name without the extension (e.g., for seq1.fasta, just type seq1).

4. Run the program
```bash
python src/main.py
```
5. Follow the prompts

- Enter the names of the two FASTA files you want to align.
- The program will read the sequences, perform a global alignment using the Needleman–Wunsch algorithm, and display the results in your terminal.

## References

- Needleman, S.B., & Wunsch, C.D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins.
- Mount, D.W. (2004). Bioinformatics: Sequence and Genome Analysis. Cold Spring Harbor Laboratory Press.
- EMBOSS Needle tool: https://www.ebi.ac.uk/jdispatcher/psa/emboss_needle
- Biopython Documentation: https://biopython.org/wiki/Documentation
- Simplified Needleman-Wunsch Algorithm inspired by: https://gist.github.com/slowkow/06c6dba9180d013dfd82bec217d22eb5
