FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# The code to run when container is started:
RUN conda install -c huggingface transformers
RUN conda install huggingface_hub=0.2.1
COPY . .
EXPOSE 7000
ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "main.py"]
#RUN /bin/bash
