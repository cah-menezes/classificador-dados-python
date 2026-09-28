# 🛡️ Classificador de Dados Sensíveis LGPD

Script em Python que analisa textos em busca de dados pessoais sensíveis conforme classificados pela Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2020).

## 🚀 Funcionalidades

* **Detecção de dados sensíveis:** identifica palavras como religião, etnia, biometria e diagnóstico no texto inserido.
* **Explicações da LGPD:** para cada dado encontrado, exibe o motivo pelo qual é considerado sensível segundo a lei.
* **Interface gráfica:** janela simples desenvolvida com `tkinter` para facilitar o uso.
* **Dois modos de uso:** via terminal (`classificador.py`) ou via interface gráfica (`interface.py`).

## 🛠️ Tecnologias Utilizadas

* Python 3 (`tkinter`, `scrolledtext`)
* Git & GitHub

## 🏁 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/cah-menezes/classificador-dados-python.git
cd classificador-dados-python
```

2. Via terminal:
```bash
python3 classificador.py
```

3. Via interface gráfica:
```bash
python3 interface.py
```

## 📝 Observações

A lógica de detecção e as explicações da LGPD foram desenvolvidas por mim. A estrutura da interface gráfica (`interface.py`) foi construída com auxílio de IA.

## 🗺️ Próximos Passos

* Expandir a lista de palavras sensíveis
* Detectar padrões como CPF e e-mail usando expressões regulares
* Melhorar o visual da interface