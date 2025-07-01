# Morgan counts fingerprints

The Morgan Fingerprints, or extended connectivity fingerprints (ECFP4) are one of the most widely used molecular representations. They are circular representations (from an atom, search the atoms around with a radius n) and can have thousands of features. This implementation uses the RDKit package and is done with radius 3 and 2048 dimensions.

This model was incorporated on 2021-09-09.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5axz`
- **Slug:** `morgan-counts`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Fingerprint`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2048`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_0000 | integer | high | Morgan count fingeprint dimension 0 with radius 3 and 2048 bits |
| dim_0001 | integer | high | Morgan count fingeprint dimension 1 with radius 3 and 2048 bits |
| dim_0002 | integer | high | Morgan count fingeprint dimension 2 with radius 3 and 2048 bits |
| dim_0003 | integer | high | Morgan count fingeprint dimension 3 with radius 3 and 2048 bits |
| dim_0004 | integer | high | Morgan count fingeprint dimension 4 with radius 3 and 2048 bits |
| dim_0005 | integer | high | Morgan count fingeprint dimension 5 with radius 3 and 2048 bits |
| dim_0006 | integer | high | Morgan count fingeprint dimension 6 with radius 3 and 2048 bits |
| dim_0007 | integer | high | Morgan count fingeprint dimension 7 with radius 3 and 2048 bits |
| dim_0008 | integer | high | Morgan count fingeprint dimension 8 with radius 3 and 2048 bits |
| dim_0009 | integer | high | Morgan count fingeprint dimension 9 with radius 3 and 2048 bits |

_10 of 2048 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5axz](https://hub.docker.com/r/ersiliaos/eos5axz)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5axz.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5axz.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `513`
- **Image Size (Mb):** `416.3`

**Computational Performance (seconds):**
- 10 inputs: `29.41`
- 100 inputs: `19.67`
- 10000 inputs: `232.11`

### References
- **Source Code**: [https://github.com/rdkit/rdkit](https://github.com/rdkit/rdkit)
- **Publication**: [https://pubs.acs.org/doi/10.1021/ci100050t](https://pubs.acs.org/doi/10.1021/ci100050t)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2010`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5axz
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5axz
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
