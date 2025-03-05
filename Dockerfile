FROM bentoml/model-server:0.11.0-py312

RUN pip install rdkit==2024.9.5
RUN pip install numpy==2.2.3

WORKDIR /repo
COPY . /repo
