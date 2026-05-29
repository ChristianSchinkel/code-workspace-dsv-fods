# Use the official Miniconda3 image as a base
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the environment.yml file to the container
COPY environment.yml .

# Create the conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "fods-env", "/bin/bash", "-c"]

# Expose the port the app runs on
EXPOSE 8888

Create a directory for the notebook
RUN mkdir -p /data/notebooks

# Set the default command to launch Jupyter Notebook
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "fods-env", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/data/notebooks"]
