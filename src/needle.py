import numpy as np
from Bio.Align import substitution_matrices

def needleman_wunsch(seq1, seq2, matrix_name="BLOSUM62", gap_open=-10, gap_extend=-0.5):
    matrix = substitution_matrices.load(matrix_name)
    
    n, m = len(seq1)+1, len(seq2)+1
    score = np.zeros((n, m))
    traceback = np.zeros((n, m), dtype=int)  # 0=diag, 1=up, 2=left

    for i in range(1, n):
        score[i][0] = gap_open + (i-1)*gap_extend
        traceback[i][0] = 1
    for j in range(1, m):
        score[0][j] = gap_open + (j-1)*gap_extend
        traceback[0][j] = 2

    for i in range(1, n):
        for j in range(1, m):
            match_score = matrix[seq1[i-1], seq2[j-1]]
            diag = score[i-1][j-1] + match_score
            up = score[i-1][j] + (gap_extend if traceback[i-1][j]==1 else gap_open)
            left = score[i][j-1] + (gap_extend if traceback[i][j-1]==2 else gap_open)
            max_score = max(diag, up, left)
            score[i][j] = max_score
            traceback[i][j] = [diag, up, left].index(max_score)

    aligned1, aligned2 = "", ""
    i, j = len(seq1), len(seq2)
    while i>0 or j>0:
        if i>0 and j>0 and traceback[i][j]==0:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i -= 1
            j -= 1
        elif i>0 and traceback[i][j]==1:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1
        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    return aligned1, aligned2, score[-1][-1]
