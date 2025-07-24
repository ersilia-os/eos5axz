import csv, json, os, struct, sys, time
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
import numpy as np

st = time.perf_counter()
input_file = sys.argv[1]
output_file = sys.argv[2]

EOS_TMP = os.path.join(os.path.join(str(Path.home()), "eos"), "temp")
BIN_FILE = os.path.join(EOS_TMP, "eos5axz_output.bin")
if os.path.exists(BIN_FILE):
  os.remove(BIN_FILE)

root = os.path.dirname(os.path.abspath(__file__))

RADIUS = 3
NBITS = 2048
mfpgen = rdFingerprintGenerator.GetMorganGenerator(radius=RADIUS, fpSize=NBITS)


def read_smiles_csv(in_file):
  with open(in_file, "r") as f:
    reader = csv.reader(f)
    cols = next(reader)
    data = [r[0] for r in reader]
    return cols, data


def read_smiles_bin(in_file):
  with open(in_file, "rb") as f:
    data = f.read()

  mv = memoryview(data)
  nl = mv.tobytes().find(b"\n")
  meta = json.loads(mv[:nl].tobytes().decode("utf-8"))
  cols = meta.get("columns", [])
  count = meta.get("count", 0)

  smiles_list = [None] * count
  offset = nl + 1
  for i in range(count):
    (length,) = struct.unpack_from(">I", mv, offset)
    offset += 4
    smiles_list[i] = mv[offset : offset + length].tobytes().decode("utf-8")
    offset += length

  return cols, smiles_list


def read_smiles(in_file):
  if in_file.endswith(".bin"):
    return read_smiles_bin(in_file)
  return read_smiles_csv(in_file)


def clip_sparse(vect, nbits):
  l = [0] * nbits
  for i, v in vect.GetNonzeroElements().items():
    l[i] = v if v < 255 else 255
  return l


def morganfp(mol):
  v = mfpgen.GetCountFingerprint(mol)
  return clip_sparse(v, NBITS)


def write_out_csv(results, header, file):
  with open(file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in results:
      writer.writerow(r)


def write_out_bin(results, header, file):
  arr = np.asarray(results, dtype=np.int32)
  meta = {"columns": header, "shape": arr.shape, "dtype": "int32"}
  meta_bytes = (json.dumps(meta) + "\n").encode("utf-8")

  with open(file, "wb") as f:
    f.write(meta_bytes)
    f.truncate(len(meta_bytes) + arr.nbytes)

  m = np.memmap(
    file, dtype=arr.dtype, mode="r+", offset=len(meta_bytes), shape=arr.shape
  )
  m[:] = arr
  m.flush()


def write_out(results, header, file):
  if file.endswith(".bin"):
    write_out_bin(results, header, file)
  elif file.endswith(".csv"):
    write_out_csv(results, header, file)
  else:
    raise ValueError(f"Unsupported extension for {file!r}")


outputs = []
empty_output = [None] * NBITS
smiles_list = read_smiles(input_file)[1]
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

headers = [f"dim_{i}" for i in range(len(outputs[0]))]

write_out(outputs, headers, output_file)
