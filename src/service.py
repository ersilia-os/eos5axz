import random
import numpy as np
import json
import collections
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rd
from typing import List

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.common import JSONArtifact
from bentoml.types import JsonSerializable


RADIUS = 3
NBITS = 2048
DTYPE = np.int8


def to_np(vect, nbits):
    arr = numpy.zeros((nbits, ), 'i')
    return ConvertToNumpyArray(vect, arr)

def clip_sparse(vect, nbits):
    l = [0]*nbits
    for i,v in vect.GetNonzeroElements().items():
        l[i] = v if v > 255 else 255
    return l


class Descriptor(object):

    def __init__(self):
        self.nbits = NBITS
        self.radius = RADIUS

    def calc(self, mol):
        v = rd.GetHashedMorganFingerprint(m, radius=self.radius, nBits=self.nbits)
        return clip_sparse(v, self.nbits)



@artifacts([JSONArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput(), batch=True)
    def calculate(self, input: List[JsonSerializable]):
        desc = Descriptor()
        input = input[0]
        output = []
        for inp in input:
            mol = Chem.MolFromSmiles(inp["input"])
            fp = np.array(desc.calc(mol), dtype=np.int8)
            output += [{"fp": fp}]
        return [output]
