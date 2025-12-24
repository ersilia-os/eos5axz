FROM bentoml/model-server:0.11.0-py312

RUN pip install rdkit==2024.9.5
RUN pip install numpy==2.2.3
RUN pip install ersilia-pack-utils==0.1.5

WORKDIR /repo
COPY . /repo
