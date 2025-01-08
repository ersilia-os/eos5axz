# imports
import os
import csv
import sys

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rd
import numpy as np

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

RADIUS = 3
NBITS = 2048


def clip_sparse(vect, nbits):
    l = [0] * nbits
    for i, v in vect.GetNonzeroElements().items():
        l[i] = v if v < 255 else 255
    return l

def morganfp(mol):
    v = rd.GetHashedMorganFingerprint(mol, radius=RADIUS, nBits=NBITS)
    return clip_sparse(v, NBITS)

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model

outputs = []
empty_output = [None]*NBITS

for smiles in smiles_list:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        outputs += [empty_output]
    fp = morganfp(mol)
    fp = np.array(fp, dtype=int)
    outputs += [fp]

# check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

header = ["dimension_{0}".format(str(i).zfill(4)) for i in range(NBITS)]

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)  # header
    for o in outputs:
        writer.writerow(o)

