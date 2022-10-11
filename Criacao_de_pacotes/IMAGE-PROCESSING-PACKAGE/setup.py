from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_98765",
    version="0.0.1",
    author="Igor Almeida da Silva",
    author_email="igor.almeidadasilva13@gmail.com",
    description="",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/igoralmeidadasilva/Desafio_de_Projeto_Criacao_de_pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)