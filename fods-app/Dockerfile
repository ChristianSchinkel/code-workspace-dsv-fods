# Use the official Miniconda3 image as a base
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the environment.yml file to the container
COPY environment.yml .

# Create the conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "dsv-fods-env", "/bin/bash", "-c"]

# Expose the port the app runs on
EXPOSE 8888

# Create the directory that Jupyter will use (absolute path)
RUN mkdir -p /data/notebooks
VOLUME /data/notebooks

# Start Jupyter Notebook with the environment
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "dsv-fods-env", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/data/notebooks"]
