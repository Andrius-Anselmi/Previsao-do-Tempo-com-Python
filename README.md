# 🌤️ Previsão do Tempo

Aplicação em Python que consome a API do [Open-Meteo](https://open-meteo.com/) para exibir a previsão do tempo dos próximos 7 dias de qualquer cidade do mundo.

## 📋 Funcionalidades

- Busca previsão do tempo por nome de cidade
- Exibe temperaturas mínimas e máximas dos próximos 7 dias
- Exporta a previsão em PDF
- Menu interativo no terminal com cores personalizáveis
- Modo alto contraste e texto maiúsculo (acessibilidade)
- API REST documentada com FastAPI

## 🗂️ Estrutura do projeto
```
├── main.py        # Menu interativo no terminal
├── previsao.py    # Funções de busca na API
├── exportar.py    # Exportação para PDF
├── api.py         # API REST com FastAPI
```

## ▶️ Como rodar

### Pré-requisitos

- Python 3.12+
- Ambiente virtual ativado

### Instalação
```bash
python3 -m venv meu_env
source meu_env/bin/activate
pip install requests fpdf2 fastapi uvicorn
```

### Rodar o menu no terminal
```bash
python3 main.py
```

### Rodar a API
```bash
uvicorn api:app --reload
```

Acesse a documentação em: `http://localhost:8000/docs`

## 🔗 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/previsao/{cidade}` | Retorna previsão em JSON |
| GET | `/previsao/{cidade}/pdf` | Baixa a previsão em PDF |

## 🛠️ Tecnologias

- Python
- Open-Meteo API
- FastAPI
- fpdf2
- Uvicorn
