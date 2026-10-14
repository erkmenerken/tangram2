from setuptools import find_packages, setup

def parse_requirements(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="tangram2",
    version="0.1+rnaquarium.1",
    description="Tangram2 (mapping installable without the optional CCC and benchmarking dependencies)",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "torch>=2.7,<2.8", "scanpy==1.11.2", "anndata==0.12.6",
        "numpy==2.2.6", "pandas==2.3.0", "scipy==1.16.0",
        "h5py==3.14.0", "wandb==0.20.1", "matplotlib==3.10.3",
        "seaborn==0.13.2", "tqdm",
    ],
)
