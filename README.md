# App de Gerenciamento de Vendas

Um aplicativo móvel desenvolvido com Kivy para gerenciamento de vendas, equipes e métricas de desempenho.

![Logo do Aplicativo](https://github.com/juanmurta/projeto-app/blob/810facfadb554777892411289b9148a091883a3f/icones/logo.png)

## 📋 Descrição

Este aplicativo foi desenvolvido para facilitar o gerenciamento de vendas e equipes de vendedores. Ele permite que os usuários registrem vendas, acompanhem métricas de desempenho, gerenciem equipes e visualizem dados de vendas de toda a empresa.

## ✨ Funcionalidades

- **Autenticação de Usuários**: Sistema de login e cadastro utilizando Firebase Authentication
- **Registro de Vendas**: Adicione vendas com informações de cliente, produto, quantidade, preço e data
- **Gerenciamento de Equipe**: Adicione e visualize vendedores da sua equipe
- **Métricas de Desempenho**: Acompanhe o total de vendas e outras métricas importantes
- **Visualização de Dados**: Veja vendas individuais ou de toda a empresa
- **Perfil Personalizável**: Altere sua foto de perfil e visualize seu ID único

## 🚀 Instalação

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/app-gerenciamento-vendas.git
```

2. Instale as dependências:
```
pip install kivy requests certifi
```

3. Execute o aplicativo:
```
python main.py
```

## 🔧 Requisitos

- Python 3.7+
- Kivy
- Requests
- Certifi

## 💻 Como Usar

1. **Login/Cadastro**: Faça login com seu e-mail e senha ou crie uma nova conta
2. **Adicionar Venda**: Clique no botão "+" na tela inicial para adicionar uma nova venda
3. **Gerenciar Equipe**: Clique no ícone de vendedor para visualizar e adicionar membros à sua equipe
4. **Configurações**: Acesse as configurações para alterar sua foto de perfil e visualizar seu ID único
5. **Visualizar Vendas**: Na tela inicial, veja todas as suas vendas e o valor total

## 🔍 Estrutura do Projeto

- **main.py**: Arquivo principal do aplicativo
- **main.kv**: Arquivo Kivy principal que define a estrutura da interface
- **myfirebase.py**: Gerencia a autenticação e comunicação com o Firebase
- **bannervenda.py**: Define o componente de exibição de vendas
- **bannervendedor.py**: Define o componente de exibição de vendedores
- **botoes.py**: Define os componentes de botões personalizados
- **telas.py**: Define as classes para as diferentes telas do aplicativo
- **kv\**: Pasta contendo arquivos Kivy para cada tela do aplicativo
- **icones\**: Pasta contendo imagens e ícones utilizados no aplicativo

## 🔐 Autenticação

O aplicativo utiliza Firebase Authentication para gerenciar usuários. Cada usuário recebe um ID único e pode gerenciar suas próprias vendas e equipe.

## 📊 Armazenamento de Dados

Os dados são armazenados no Firebase Realtime Database, permitindo sincronização em tempo real entre dispositivos.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📱 Compatibilidade

O aplicativo é compatível com dispositivos Android e iOS, graças ao framework Kivy.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## 📞 Contato

Para mais informações, entre em contato através do e-mail: juanmurta@gmail.com
