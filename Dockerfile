FROM bentoml/model-server:0.11.0-py310

RUN pip install rdkit==2022.9.5
RUN pip install numpy==1.26.4

WORKDIR /repo
COPY . /repo
