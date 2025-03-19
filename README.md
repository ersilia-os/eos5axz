# Morgan counts fingerprints

**Description:**  
The Morgan Fingerprints, or extended connectivity fingerprints (ECFP4) are one of the most widely used molecular representations. They are circular representations (from an atom, search the atoms around with a radius n) and can have thousands of features. This implementation uses the RDKit package and is done with radius 3 and 2048 dimensions.


## Identifiers:
- **Ersilia Identifier:** `eos5axz`
- **Slug:** `morgan-counts`

## Domain:
- **Task:** Representation
- **Subtask:** Featurization
- **Biomedical Area:** Any
- **Target Organism:** Not Applicable
- **Tags:** Fingerprint, Descriptor

## Input:
- **Input:** Compound
- **Input Dimension:** 1

## Output:
- **Output:** 
- **Output Dimension:** 2048
- **Output Consistency:** Fixed
- **Interpretation:** Vector representation of a molecule

- **Output Columns** (up to 10):

| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_0000 | integer |  | Morgan count fingeprint dimension 0 with radius 3 and 2048 bits |
| dim_0001 | integer |  | Morgan count fingeprint dimension 1 with radius 3 and 2048 bits |
| dim_0002 | integer |  | Morgan count fingeprint dimension 2 with radius 3 and 2048 bits |
| dim_0003 | integer |  | Morgan count fingeprint dimension 3 with radius 3 and 2048 bits |
| dim_0004 | integer |  | Morgan count fingeprint dimension 4 with radius 3 and 2048 bits |
| dim_0005 | integer |  | Morgan count fingeprint dimension 5 with radius 3 and 2048 bits |
| dim_0006 | integer |  | Morgan count fingeprint dimension 6 with radius 3 and 2048 bits |
| dim_0007 | integer |  | Morgan count fingeprint dimension 7 with radius 3 and 2048 bits |
| dim_0008 | integer |  | Morgan count fingeprint dimension 8 with radius 3 and 2048 bits |
| dim_0009 | integer |  | Morgan count fingeprint dimension 9 with radius 3 and 2048 bits |

_Total columns: 2048_
## Source and Deployment:
- **Source:** Local
- **Source Type:** External
- **[DockerHub](https://hub.docker.com/r/ersiliaos/eos5axz)**
- **Docker Architecture:** AMD64, ARM64
- **[S3 Storage](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5axz.zip)**

## Resource Consumption:
- **Model Size:** 1
- **Environment Size:** 496


## References:
- **[Source Code](https://github.com/rdkit/rdkit)**
- **[Publication](https://pubs.acs.org/doi/10.1021/ci100050t)**
  - **Publication Type:** Peer reviewed
  - **Publication Year:** 2010
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

## License:
This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

**Notice**: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Ersilia:
The [Ersilia Open Source Initiative](https://ersilia.io) is a non-profit organization fueling sustainable research in the Global South.

[Help us](https://www.ersilia.io/donate) achieve our mission!