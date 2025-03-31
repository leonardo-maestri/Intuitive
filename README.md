# 📌 Projeto ANS - Pipeline de Dados Completo

Automatiza a coleta, processamento e disponibilização de dados de operadoras de saúde.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/PostgreSQL-13%2B-blue?logo=postgresql">
  <img src="https://img.shields.io/badge/Flask-2.0-lightgrey?logo=flask">
  <img src="https://img.shields.io/badge/Vue.js-3.x-brightgreen?logo=vue.js">
</div>

## 📋 Visão Geral


- 🔹 Download automático de PDFs do portal da ANS
- 🔹 Extração e transformação de tabelas PDF → CSV
- 🔹 Criação de banco de dados PostgreSQL
- 🔹 Inserção de Dados nas Tabelas com Arquivos CSV
- 🔹 API REST com busca inteligente em dados de operadoras
- 🔹 Interface web para consulta interativa

## ⚙️ Funcionalidades

### ✅ Web Scraping
- Download automatizado de Anexos I e II em PDF
- Compactação dos arquivos em ZIP


### ✅ ETL (Extract, Transform, Load)
- Extração de tabelas de PDFs usando `tabula-py`
- Tratamento de Dados
- Geração de CSV estruturado


### ✅ Banco de Dados
- Criação automática de tabelas no PostgreSQL
- Carga de dados a partir de CSV
- Queries analíticas 


### ✅ Backend
- Servidor Python
- API Flask com endpoints RESTful

  
### ✅ Frontend
- Interface Vue.js responsiva
- Visualização de detalhes por operadora
