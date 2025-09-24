# Projeto de Apresentação em LaTeX

## Introdução
Esse projeto contém o código usado no trabalho principal da materia Pesquisa Operacional que foi cursado no primeiro semestre de 2025. O objetivo do que foi desenvolvido aqui é criar e resolver um modelo de programação linear para a organização de armazéns de bobinas de aço. 
Mas detalhes estão nas apresentações e artigo em LaTex presentes neste repositório.

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

Clone este repositório usando o comando abaixo:
```sh
git clone <URL_DO_REPOSITORIO>
cd <nome_da_pasta_do_projeto>
```

### 2. Instalar dependências

Certifique-se de ter as seguintes dependências instaladas no seu sistema:

- **Git**: para clonar e versionar o repositório.
- **LaTeX**: distribuição recomendada [TeX Live](https://www.tug.org/texlive/) (Linux/macOS) ou [MikTeX](https://miktex.org/) (Windows).
- **Make**: normalmente já vem instalado em sistemas Unix (Linux/macOS). No Windows, pode ser instalado via [Chocolatey](https://chocolatey.org/) ou [Gow](https://github.com/bmatzelle/gow).

#### Instalação no Ubuntu/Debian:
```sh
sudo apt update
sudo apt install git make texlive-full
```

#### Instalação no macOS (com Homebrew):
```sh
brew install git make mactex
```

#### Instalação no Windows:
- [Git para Windows](https://git-scm.com/download/win)
- [MikTeX](https://miktex.org/download)
- [Make via Chocolatey](https://community.chocolatey.org/packages/make) (opcional)

### Primeira configuração

Execute o comando abaixo para configurar os hooks do git:
```sh
./setup-hooks.sh
```


### 3. Compilar os documentos projeto

Execute o comando abaixo na raiz do documento para gerar o PDF na pasta `build/`:
```sh
make
```
O PDF final será gerado em `build/<nome-do-documento>.pdf`.

Para limpar os arquivos temporários e o PDF gerado:
```sh
make clean
```

## Visual Studio Code: Extensões recomendadas

Ao abrir este projeto no VSCode, você receberá sugestões automáticas de extensões úteis para trabalhar com LaTeX e com a estrutura do repositório. As recomendações ficam no arquivo `.vscode/extensions.json` e incluem, por exemplo:
- **James-Yu.latex-workshop**: suporte completo a LaTeX no VSCode.
- **PKief.material-icon-theme**: ícones de pastas e arquivos mais intuitivos.

Assim, você terá uma experiência de desenvolvimento mais produtiva e integrada.

## Recomendação de IDE

Recomenda-se o uso do Visual Studio Code (VSCode) para desenvolver o projeto.
Para pessoas que tem interesse em usar mais IA recomendo fortemente o uso da IDE
Cursor. Ou pelo menos do github copilot.
