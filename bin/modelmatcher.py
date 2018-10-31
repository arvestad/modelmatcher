#!/usr/bin/env python3

import argparse
import os
import sys
from traceback import print_last
from Bio import AlignIO

from models import RateMatrix

_ALPHABET = 'ARNDCQEGHILKMFPSTWYV'

def guess_format(filename):
    '''
    Returns a string that guesses the MSA format used in filename.
    '''
    with open(filename) as h:
        first_line = h.readline()
        if first_line[:15] == '# STOCKHOLM 1.0':
            return 'stockholm'
        elif first_line == 'CLUSTAL':
            return 'clustal'
        elif first_line[0] == '>':
            return 'fasta'
        elif first_line.lower().startswith("#nexus"):
            return 'nexus'
        else:
            tokens = first_line.split()
            if len(tokens) != 2:
                raise Exception(f'Does not recognize the format in {filename}')
            else:
                try:            # If the first line contains two integers, then it ought to be Phylip
                    a = int(tokens[0])
                    b = int(tokens[1])
                except:
                    raise Exception(f'Does not recognize the format in {filename}')
                # Came this far? Success!
                return 'phylip'
            

def read_alignment(file, input_format):
    '''
    Factory function. Read the alignment with BioPython's support, and 
    return an appropriate alignment.
    '''
    if file == '-':
        file = sys.stdin        # Start reading from stdin if "magic filename"
    elif input_format == 'guess':
        seqtype = guess_format(file)
    alignment = AlignIO.read(file, input_format)
    return alignment


import numpy as np

def create_count_matrix(s1, s2):
    return_matrix = np.zeros((20,20))
    f_vec = np.zeros(20)

    alphabet_dictionary = {}
    for i, letter in enumerate(_ALPHABET):
        alphabet_dictionary[letter] = i

    for a, b in zip(s1, s2):
        try:
            i = alphabet_dictionary[b]
            j = alphabet_dictionary[a]
            return_matrix[i][j] = return_matrix[i][j] + 1
            f_vec[i] += 1
            f_vec[j] += 1
        except KeyError as e:
            if a not in '.-' or b not in '.-':
                raise e
            # else we just continue because we don't care about indels

    return return_matrix, f_vec


import itertools as it
def msa_to_count_matrix(msa):
    sequences = map(lambda r: r.seq, msa)
    m_sum = np.zeros((20, 20))
    f_vec = np.zeros(20)
    for a, b in it.combinations(sequences, 2):
        m, f = create_count_matrix(a, b)
        np.add(m_sum, m, m_sum)  # Add m_sum and m, and put the result in m_sum
        np.add(f_vec, f, f_vec)
    symmetric = np.add(m_sum, m_sum.T)
    scale = np.sum(f_vec)
    return symmetric, f_vec/scale


def diagonalize_with_model(m, Q):
    '''
    Try to diagonalize m using the eigenvectors of Q and the equilibrium distribution.
    Return the sum of the off-diagonal elements of what was supposed to be the 
    diagonal matrix.
    '''
    off_diagonal_elems = np.ones((20,20))
    np.fill_diagonal(off_diagonal_elems, 0) # Set the diagonal to zero

    L_ev, R_ev = Q.get_eigenvectors()

    right_product = np.matmul(m, R_ev)
    f = Q.get_freq()
    left = np.matmul(L_ev, np.diag(1.0/f))
    prod = np.matmul(left, right_product)
    off_diagonal = prod * off_diagonal_elems
    return np.sum(np.absolute(off_diagonal)) # Measure the deviation as sum of off-diagonal elements
    
def apply_models(m, aa_freqs):
    '''
    Try eigenvectors of standard rate matrices aginst the count matrix m
    '''
    matrices= RateMatrix.get_all_models()
    diffs = []
    for Q in matrices:
        diff = diagonalize_with_model(m, Q)
        diffs.append((Q.get_name(), diff))

        # Now Q+F
        # Q.update_freq(aa_freqs)
        # diff = diagonalize_with_model(m, Q)
        # diffs.append((Q.get_name() + '+F', diff))

    return diffs

def main(filename):
    msa = read_alignment(filename, 'phylip')
    N, amino_acid_freqs = msa_to_count_matrix(msa)
    F = N / np.sum(N)
    diffs = apply_models(F, amino_acid_freqs)
    for name, d in sorted(diffs, key = lambda d: d[1]):
        print(f'{name:12} {d:>8.3f}')

if __name__ == '__main__':
    # For convenience, set some print options for numpy
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    np.set_printoptions(linewidth=200)
    main(sys.argv[1])
