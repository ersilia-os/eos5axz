# Morgan counts fingerprints

The Morgan Fingerprints, or extended connectivity fingerprints (ECFP4) are one of the most widely used molecular representations. They are circular representations (from an atom, search the atoms around with a radius n) and can have thousands of features. This implementation uses the RDKit package and is done with radius 3 and 2048 dimensions.

## Identifiers

* EOS model ID: `eos5axz`
* Slug: `morgan-counts`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Integer`
* Output Shape: `List`
* Interpretation: Vector representation of a molecule

## References

* [Publication](https://www.rdkit.org/docs/RDKit_Book.html)
* [Source Code](https://github.com/rdkit/rdkit)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos5axz)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5axz.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos5axz) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.rdkit.org/docs/RDKit_Book.html) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!