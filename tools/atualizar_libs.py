import os

from rich.console import Console

console = Console()

def atualizar_libs():
    console.log("Iniciando o processo de atualização das libs")
    console.log("Garantindo que todas as libs estao instaladas")
    os.system("pip install -r requirements.txt")

    console.log("Lendo o arquivo de requisitos (`requirements.txt`)")
    with open("requirements.txt") as arquivo:
        libs = [linha.split("==")[0] for linha in arquivo.readlines()]

        for nome_da_lib in libs:
            console.log(f"atualizando a lib: {nome_da_lib}")
            os.system("pip install --upgrade " + nome_da_lib)

    console.log("Finalizando o processo de atualização das libs")

    console.log("Atualizando os arquivos de requisitos")
    os.system("pip freeze > requirements.txt")
    os.system("pip freeze > requirements-dev.txt")

if __name__ == "__main__":
    atualizar_libs()
