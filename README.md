# 🐍 [PETD] Aula 05 — Trabalho Prático · WeatherNow

> Programação Estruturada e Tipos de Dados · CTeSP em Redes e Sistemas Informáticos · ISTEC Porto · 2025/2026

---

## 📋 Informações da UC

| Campo | Detalhe |
|---|---|
| **Unidade Curricular** | Programação Estruturada e Tipos de Dados (PETD) |
| **Docente** | Mário Amorim |
| **Curso** | CTeSP em Redes e Sistemas Informáticos |
| **Período** | 2.º Semestre |
| **Ano** | 1.º Ano |
| **Ano Letivo** | 2025/2026 |
| **Aluno** | Gonçalo Lopes Fernandes (N.º 2022148) |
| **Nota Final** | A aguardar (publicação prevista em julho 2026) |

---

## 📁 Estrutura do Repositório

```
petd-aula05-trabalho-pratico/
├── docs/                                              # Documentação do projeto
│   └── PETD-Relatorio-Tecnico-WeatherNow.docx         # Relatório técnico do projeto
├── src/                                               # Código-fonte
│   ├── backend/                                       # Backend Python (FastAPI)
│   │   ├── main.py                                    # Ponto de entrada da API
│   │   ├── weather_service.py                         # Módulo de comunicação com OpenWeatherMap
│   │   ├── config.py                                  # Configurações e variáveis de ambiente
│   │   └── requirements.txt                           # Dependências Python
│   └── frontend/                                      # Frontend móvel
│       └── weathernow_app/                            # Aplicação Flutter (Dart)
│           └── .gitkeep
├── .gitignore
└── README.md
```

---

## 📝 Trabalhos Realizados

### 1. Projeto WeatherNow — Aplicação Móvel de Consulta Meteorológica

Trabalho prático desenvolvido para avaliação da UC de PETD, com peso de **40% da nota final** (Trabalhos práticos 20% + Trabalho Final 20%), com nota mínima de 7,5 valores. Inclui Projeto, Relatório e Defesa.

**WeatherNow** é uma aplicação móvel que permite ao utilizador consultar as condições meteorológicas atuais para qualquer localização, seguindo uma arquitetura cliente-servidor:

- **Frontend (Flutter/Dart)** — Aplicação Android distribuída via APK, com interface Material Design para introdução da localização e apresentação dos dados meteorológicos.
- **Backend (Python/FastAPI)** — API REST que recebe os pedidos do Flutter, comunica com a API gratuita do OpenWeatherMap, processa a resposta JSON e devolve os dados formatados ao cliente.
- **Hosting (Render)** — O backend é alojado na plataforma Render (plano gratuito), garantindo que a aplicação está acessível publicamente e que a chave da API nunca é exposta no código do cliente.

**Fluxo da aplicação:** O utilizador instala o APK, introduz a cidade desejada, o Flutter envia um pedido HTTP ao backend Python no Render, que por sua vez consulta a API do OpenWeatherMap e devolve os dados meteorológicos (temperatura, descrição, humidade, vento) para apresentação na interface.

### 2. Relatório Técnico

Foi elaborado um relatório técnico completo (`PETD-Relatorio-Tecnico-WeatherNow.docx`) que documenta a arquitetura, stack tecnológica, fluxo da aplicação, conceitos de PETD aplicados, requisitos funcionais e não funcionais, interface e cronograma de desenvolvimento.

---

## 🧠 Temas Abordados na UC (Aplicados no Projeto)

| Tema | Aplicação no Projeto |
|---|---|
| Tipos de dados | `str` (localização), `float` (temperatura), `int` (humidade), `dict` (JSON), `bool` (validações) |
| Funções (`def`, `return`) | Funções para chamada à API, parsing de JSON e formatação de resposta |
| Parâmetros e `*args` | Funções com parâmetros opcionais (unidades, idioma, timeout) |
| Módulos e `import` | Separação em módulos (`weather_service`, `config`, `main`) |
| Tratamento de erros | `try`/`except` para falhas de rede, cidade não encontrada, API indisponível |
| F-strings e formatação | Construção de URLs e formatação de respostas |
| Dicionários | Parsing da resposta JSON da API (estrutura chave-valor) |
| Ficheiros | Leitura de configurações e gestão de variáveis de ambiente |

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia | Detalhes |
|---|---|---|
| Frontend | Flutter (Dart) | Aplicação Android com interface Material Design |
| Backend | Python + FastAPI | API REST assíncrona |
| Hosting | Render | Plano gratuito para Web Services |
| API Externa | OpenWeatherMap | API meteorológica gratuita (1.000 chamadas/dia) |

---

## 📬 Contacto

**Gonçalo Lopes Fernandes**
📧 goncalo.fernandes.2022148@my.istec.pt

---

*Repositório académico criado no âmbito do CTeSP em Redes e Sistemas Informáticos — ISTEC Porto, 2025/2026.*
