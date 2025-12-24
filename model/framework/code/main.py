import csv, json, os, struct, sys, time
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
import numpy as np
from ersilia_pack_utils.core import write_out, read_smiles

st = time.perf_counter()
input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))

RADIUS = 3
NBITS = 2048
mfpgen = rdFingerprintGenerator.GetMorganGenerator(radius=RADIUS, fpSize=NBITS)

def clip_sparse(vect, nbits):
  l = [0] * nbits
  for i, v in vect.GetNonzeroElements().items():
    l[i] = v if v < 255 else 255
  return l

def morganfp(mol):
  v = mfpgen.GetCountFingerprint(mol)
  return clip_sparse(v, NBITS)

outputs = []
empty_output = [None] * NBITS
_, smiles_list = read_smiles(input_file)
for smiles in smiles_list:
  mol = Chem.MolFromSmiles(smiles)
  if mol is None:
    outputs += [empty_output]
  fp = morganfp(mol)
  fp = np.array(fp, dtype=int)
  outputs += [fp]
et = time.perf_counter()
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

headers = ["dim_{0}".format(str(i).zfill(4)) for i in range(len(outputs[0]))]

write_out(outputs, headers, output_file, np.float32)
