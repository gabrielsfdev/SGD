# Plataforma de Gerenciamento de Imagens de Documentos Pessoais

## Projeto de Conclusão de Ciclo - Equipe Python Hard

---

## Descrição do Projeto

Este é um Sistema que gerencia documentos pessoais, coleta os dados a partir da imagem, identificação de informações e armazenamento eficientes destas. O objetivo é desenvolver um sistema que simplifique os processos de coleta, reconhecimento óptico de caracteres (OCR), armazenamento seguro e recuperação ágil de imagens de documentos pessoais.

## Requisitos

- Utilização de banco de dados relacional através do SQLAlchemy para armazenamento.
- Implementação de autenticação e gestão de usuários, incluindo funcionalidades como registro, login e logout.
- Desenvolvimento da interface utilizando Tkinter.
- Utilização do OpenCV para leitura de imagens e do Pytesseract para reconhecimento óptico de caracteres (OCR).

---

## Coleta de Documentos

### Descrição

O algoritmo de coleta de documentos foi desenvolvido para identificar e extrair informações de imagens fornecidas pelo usuário. Embora não seja responsabilidade da equipe buscar os documentos, é nossa responsabilidade garantir a eficiência do processo de coleta.

### Funcionalidades Principais

- Identificação e extração de imagens nos formatos .jpeg ou .jpg.
- Conversão de formatos de imagem diferentes, se necessário.
- Disponibilização das imagens coletadas para processamento adicional.

### Utilização

Para utilizar o algoritmo, é necessário fornecer os documentos como entrada para serem armazenados. O algoritmo depende do OpenCV para processamento de imagem em Python.

### Exemplo de Utilização

1. O usuário faz o upload de um documento através da interface do sistema.
2. O algoritmo de coleta identifica e extrai as informações relevantes da imagem.
3. O documento é armazenado no banco de dados para recuperação posterior.

---

## Tratamento de Imagens e Reconhecimento de Texto

### Descrição

O processo de tratamento de imagens e reconhecimento de texto visa melhorar a qualidade das imagens e extrair o texto nelas presente. Isso é feito através do pré-processamento das imagens e do uso de técnicas de OCR.

### Funcionalidades Principais

- Carregamento e pré-processamento das imagens.
- Reconhecimento óptico de caracteres (OCR) utilizando a biblioteca pytesseract.
- Reconhecimento do tipo de documentação presente na imagem.

### Utilização

O texto extraído é disponibilizado para utilização pela equipe, podendo ser analisado, indexado ou utilizado em outras tarefas do projeto.

---

## Armazenamento e Recuperação

### Descrição

O sistema de armazenamento e recuperação utiliza um banco de dados relacional (SQLite) para armazenar e recuperar documentos pessoais de forma segura e eficiente.

### Funcionalidades Principais

- Armazenamento seguro de documentos.
- Indexação e busca eficientes.
- Interface intuitiva para navegação e recuperação de documentos.

### Utilização

Os documentos são armazenados com mecanismos de controle de acesso para garantir a privacidade e confidencialidade das informações.

---

## Interface do Sistema

### Descrição

A interface do sistema foi desenvolvida visando proporcionar uma experiência de usuário intuitiva e eficiente utilizando Tkinter. Possui um design claro e organizado, compatível com diversos dispositivos.

### Características Principais

- Design intuitivo e amigável.
- Funcionalidades de registro, login e logout.
- Visualização e manipulação de documentos.
- Compatibilidade com múltiplos dispositivos.

### Telas Principais

- Tela de Login
- Tela de Cadastro
- Tela de Esqueci a Senha
- Tela de Envio de Arquivo
- Tela de Verificação de Dados Exclusivos do Arquivo

---

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga estas etapas:

1. Fork do repositório.
2. Crie um branch para sua nova funcionalidade (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -am 'Adicionar nova funcionalidade'`).
4. Faça push para o branch (`git push origin feature/nova-funcionalidade`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

Este README fornece uma visão geral do projeto de conclusão de ciclo da equipe Python Hard, incluindo suas funcionalidades principais, requisitos e tarefas associadas. Para mais detalhes sobre cada aspecto do projeto, consulte a documentação e o código-fonte fornecidos. A equipe de desenvolvimento está disponível para suporte e melhorias contínuas conforme necessário.
