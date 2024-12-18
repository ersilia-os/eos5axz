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
    return

def morganfp(mol):
    v = rd.GetHashedMorganFingerprint(mol, radius=RADIUS, nBits=NBITS)
    return clip_sparse(v, NBITS)

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model

outputs = list(
    map(
        lambda x: np.array(morganfp(Chem.MolFromSmiles(x)), dtype=np.uint8), smiles_list
    )
)

# check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow(o)
