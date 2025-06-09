# Tradutor de Texto em Python (Procedural)

Este projeto é uma aplicação de tradução de textos desenvolvida em Python utilizando o paradigma **procedural**, com interface gráfica feita em Tkinter. A aplicação permite traduzir textos entre diferentes idiomas e oferece a funcionalidade de adicionar novas palavras e suas traduções a um dicionário interno.

---

## Funcionalidades

- Tradução de textos entre Português, Inglês, Espanhol, Francês e Alemão.
- Dicionário interno para traduções customizadas.
- Possibilidade de adicionar novas palavras e suas traduções ao dicionário.
- Interface gráfica simples e intuitiva desenvolvida com Tkinter.
- Não utiliza programação orientada a objetos nem frameworks externos além do Tkinter e googletrans.

---

## Tecnologias Utilizadas

- Python 3
- Biblioteca Tkinter para interface gráfica
- Biblioteca `googletrans` para tradução automática

---

## Como usar

### Pré-requisitos

- Python 3 instalado
- Instalar biblioteca `googletrans` versão 4.0.0-rc1 (ou mais recente)

```bash
pip install googletrans==4.0.0-rc1
Execução
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/Gnomoph/meu-projeto.git
Acesse a pasta do projeto:

bash
Copiar
Editar
cd meu-projeto
Execute o programa:

bash
Copiar
Editar
python meu_tradutor.py
Como funciona
Digite o texto que deseja traduzir na área “Texto para traduzir”.

Selecione o idioma de destino no menu suspenso.

Clique em “Traduzir” para ver o texto traduzido.

Para adicionar uma palavra nova ao dicionário, use a função “Adicionar Palavra” (detalhes no código).

Estrutura do código
O código está organizado de forma procedural, usando funções simples para:

Gerenciar a interface com Tkinter

Realizar tradução usando o googletrans

Manipular um dicionário interno para traduções customizadas

Autor
João e gabriel
Disciplina: Programação de Computadores
Professor: Jeofton Costa Melo

Licença
Este projeto foi desenvolvido para fins acadêmicos e está aberto para uso pessoal e educacional.
