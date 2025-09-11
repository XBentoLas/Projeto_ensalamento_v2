<div align="center">
  <img src="http://metodista.br/@@site-logo/logo-metodista.png" alt="Logo UMESP" width="150">
  <h1>Projeto de Ensalamento Automático</h1>
</div>

<p align="center">
Projeto de Extensão universitaria da <a href="https://www.metodista.br/">Universidade Metodista de São Paulo</a> para criar um sistema web que auxilia a coordenação na alocação automática de turmas em salas.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-blue" alt="Docker">
</p>

---

## 🎯 Objetivo
O objetivo deste projeto é desenvolver uma aplicação web que otimize e automatize o processo de ensalamento, levando em consideração as necessidades das turmas (quantidade de alunos, recursos necessários, acessibilidade) e a disponibilidade das salas, simplificando um processo complexo e manual para a coordenação dos cursos.

---

## ✨ Funcionalidades

- [x] Estrutura base do projeto com Flask ✅  
- [x] Containerização da aplicação com Docker ✅  
- [x] Página inicial (Home) com HTML/CSS básico ✅  
- [ ] Algoritmo para proessamento e ensalamento automático ⚠️
- [ ] Cadastro, Leitura, Atualização e Deleção (CRUD) de Salas ❌
- [ ] CRUD de Disciplinas ❌  
- [ ] CRUD de Turmas ❌  
- [ ] Sistema de login para usuários (Coordenação) ❌    
- [ ] Visualização do ensalamento em formato de grade ou tabela ❌  
- [ ] Geração de relatórios de ensalamento ❌  

---

## 💻 Tecnologias Utilizadas

- **Backend:** Python 3.9, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Banco de Dados:** MySQL  
- **Containerização:** Docker e Docker Compose  

---

## 🚀 Guia Rápido: Rodando o Projeto Localmente

Siga estes 5 passos para configurar e executar o projeto em sua máquina.

### Passo 1: Instale os Pré-requisitos
Antes de tudo, garanta que você tenha as seguintes ferramentas instaladas:

- [Git](https://git-scm.com/downloads) – Usado para baixar o código do repositório.  
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) – Responsável por criar o ambiente e executar nossa aplicação (já inclui o Docker Compose).  

> ✅ **Lembrete**: Você não precisa instalar Python ou Flask diretamente no seu computador. O Docker cuida de tudo para você!

### Passo 2: Baixe o Código do Projeto
Abra seu terminal e rode os seguintes comandos:

```bash
git clone https://github.com/XBentoLas/Projeto_ensalamento_v2.git
cd Projeto_ensalamento_v2
```
### Passo 3: Execute a Aplicação com Docker

Com o terminal aberto na pasta do projeto, rode:
```bash
docker-compose up --build
```

⚠️ A primeira execução pode demorar alguns minutos (Docker vai baixar as dependências).
Nas próximas vezes, será bem mais rápido.

### Passo 4 – Acessar o Site  

Assim que o servidor estiver rodando, abra o navegador e acesse:  

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)  


### Passo 5 – Encerrar o Projeto  

Para desligar o ambiente:  

1. No terminal em execução, pressione **Ctrl + C**  
2. Em seguida, rode:  

```bash
docker-compose down
```
## 🤝 Contribuidores

Gabriel Bento
