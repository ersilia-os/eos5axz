import csv
import sys
import os
import numpy as np
import joblib

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rd


ROOT = os.path.dirname(os.path.abspath(__file__))

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

# calculate morgan fingerprints
RADIUS = 3
NBITS = 2048
DTYPE = np.int8


def clip_sparse(vect, nbits):
    l = [0] * nbits
    for i, v in vect.GetNonzeroElements().items():
        l[i] = v if v < 127 else 127
    return l


class Descriptor(object):
    def __init__(self):
        self.nbits = NBITS
        self.radius = RADIUS

    def calc(self, mol):
        v = rd.GetHashedMorganFingerprint(mol, radius=self.radius, nBits=self.nbits)
        return clip_sparse(v, self.nbits)


desc = Descriptor()

X = np.zeros((len(smiles), NBITS), dtype=np.int8)
for i, smi in enumerate(smiles):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        continue
    fp = np.array(desc.calc(mol), dtype=np.int8)
    X[i] = fp

# run maip predictions
model = joblib.load(os.path.join(ROOT, "..", "checkpoints", "random_forest.joblib"))

preds = model.predict(X)

# write output
with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["score"])
    for p in preds:
        writer.writerow([p])
