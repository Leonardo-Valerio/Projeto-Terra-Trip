
# Terra Trip - Seu Guia de Viagens

Bem-vindo ao Terra Trip, seu guia de viagens personalizado! Este projeto é uma plataforma que visa fornecer informações detalhadas sobre continentes, países, cidades e pontos turísticos ao redor do mundo. 

# Sumário
1. [Sobre o Projeto](#sobre-o-projeto)

2. [Como Executar Localmente](#como-executar-o-projeto-localmente)

3. [Link do vídeo do projeto rodando](#link-do-vídeo-do-projeto)

4. [Imagens do projeto](#imagens-do-projeto)

## Sobre o Projeto

O Terra Trip é construído usando o framework web Django, oferecendo uma estrutura robusta e segura para fornecer informações de viagens. Aqui estão alguns dos principais recursos e componentes do projeto:

### Models

O banco de dados é composto por quatro modelos principais:

## App Home (referente aos destinos para o usuário escolher)

1. **Continentes**: Armazena informações sobre os continentes, incluindo nome, imagem, legenda e descrição.

2. **Paises**: Representa os países, com detalhes como nome, imagem, legenda, descrição e relação com o continente correspondente. Além disso, existem campos booleanos que indicam características especiais, como popularidade, estações recomendadas e mais.

3. **Cidades**: Contém informações sobre cidades, incluindo nome, legenda e relação com o país associado.

4. **Pontos_turisticos**: Armazena dados sobre pontos turísticos, como nome, imagens, legenda, coordenadas de latitude e longitude, e a cidade associada.

## App Usuarios 

1. **Username**: Usuário insere seu nome de user
   
2. **Senha**: Usuário insere sua senha, onde a mesma é criptografada pelo Django
   
3. **Email**: Armazena o e-mail que o usuário preenche no formulário de cadastro

## App Roteiros

1. **Nome**: Armazena o nome que o usuário definir para aquele roteiro

2. **Dias**: Armazena os dias que aquele usuário escolher para aquele roteiro

3. **Epoca**: Permite com que o usuário insira uma das 4 estações do ano que ele pensa em fazer essa viagem

4. **Usuario_roteiro**: Esse campo o usuário não escolhe, ele é preenchido na minha views quando o usuário está logado

5. **Grupo_paises**: Esse campo é preenchido quando o usuário adiciona algum país nesse roteiro, ou seja, ele começa como um array vazio e vai sendo preenchido em formato Json dos países que o usuário for adicionando nesse roteiro

### Views

As views no arquivo `views.py` controlam a lógica de renderização das páginas HTML. Destacam-se as seguintes views:

## App Home

- **index**: Apresenta a página inicial com informações sobre continentes e destaques de países em diferentes categorias.

- **continente**: Exibe informações detalhadas sobre um continente específico, incluindo países destacados em várias categorias.

- **pais**: Mostra detalhes sobre um país específico, incluindo cidades e pontos turísticos associados.

- **sobre_nos**: Apresenta uma página informativa sobre o Terra Trip e sua missão.

- **buscar**: Retorna a página de busca e nela é passado o país que o usuário envia na requisição pelo input de buscar que fica no index e na página de continentes do site. 

## App Usuarios

- **login**: Permite o usuário a fazer login de acordo com os usuários existentes cadastrados no banco de dados (para acessar algumas páginas do site é necessário que o usuário esteja logado).
  
- **cadastro**: Permite o usuário se cadastrar desde que o seu username já não exista no banco de dados.

- **logout**: Permite o usuário fazzer o logout do site

## App Roteiros:

- **todos_roteiros**: Exibe para o usuário todos os roteiros que ele tem na conta e também permite com que ele adicione um novo roteiro, preenchendo um formulário que puxa valores do meu models.py

- **roteiros**: Aqui tem a lógica para o usuário adicionar um país para o roteiro que ele escolher, desde que esse país já não esteja adicionado no roteiro escolhido, aqui ele também permite com que o usuário gere um roteiro personalizado pela IA do Chat-GPT, para isso o usuário clica num botão de gerar roteiro, é passado para a API do GPT, o grupo de paises que pertence a este roteiro, os dias estipulados dessa viagem e a estação do ano que ela vai ocorrer, a resposta da API é preenchida no campo roteiro_gerado do meu models.py do app Roteiros (se o usuário atualizar o roteiro dele, com países novos ou otra alteração), é possivel ele pedir para a IA atualizar o roteiro gerado.

- **editar_roteiro**: Permite com que o usuário faça as alterações desejadas naquele roteiro, podendo alterar os dias, estação do ano e nome.

- **deletar_roteiro**: Permite com que o usuário delete aquele roteiro que ese escolher.

- **remover_pais_roteiro**: Permite com que na página do roteiro que o usuário clicar, ele consiga excluir do roteiro dela aqueles países que ela não deseja mais para aquela viagem.

### Templates

Os templates em HTML, localizados no diretório `templates`, fornecem a estrutura visual das páginas. O uso de blocos facilita a extensão e personalização de cada página.

### Admin

O Django admin é utilizado para gerenciar o conteúdo do banco de dados de maneira eficiente. Os modelos estão registrados no arquivo `admin.py`, permitindo fácil acesso e edição pelos administradores do sistema.

### Estilo e Interatividade

O Terra Trip possui um design responsivo e utiliza a biblioteca Leaflet para incorporar mapas interativos, permitindo aos usuários visualizar a localização dos pontos turísticos.

## Como Executar o Projeto Localmente

1. **Clone o Repositório:**
git clone https://github.com/Leonardo-Valerio/Projeto-Terra-Trip.git
cd Projeto-Terra-Trip

2. **Crie e Ative o Ambiente Virtual:**
python -m venv venv
source venv/bin/activate # No Windows, use 'venv\Scripts\activate'

3. **Instale as Dependências:**
pip install -r requirements.txt

4. **Execute as Migrações:**
python manage.py migrate

5. **Crie um Usuário:**
- Vá para a tela de cadastro e faça o cadastro para criar seu usuário.

6. **Execute o Servidor de Desenvolvimento:**
python manage.py runserver

7. **Acesse o Admin:**
- Vá para a tela de login e faça o acesso com as credenciais do rusuário.

8. **Explore o Terra Trip:**
- Acesse `http://127.0.0.1:8000/` e comece a explorar o Terra Trip!

### Link do vídeo do projeto
https://www.youtube.com/watch?v=4XC-_VGAgoM
### Imagens do projeto
- **Home**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/42b792fe-cce3-4f0b-8738-66efcf9dc247)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/b9b79a9f-e371-486d-b30c-791f473a8e84)

- **Ao clicar no card do continente é levado para essa página dos países filtrado pelo continente selecionado**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/f2501b82-b323-4d1a-8b95-be1c9a198a4c)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/ce0aa5cf-3fb4-4243-b349-1b92dea1f39b)


- **Ao clicar no card do país é levado para essa página do país onde mostra as principais cidades e atrações filtrado pelo país selecionado**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/b2219f7f-267e-4b40-80f0-3a4abbbdfc58)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/0dacea5d-9654-44e5-968d-8e02fcc271b5)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/82dda127-c954-436e-8822-808cc9eb187b)

- **Ao clicar em adicionar roteiro na página do país escolhido**
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/e9d65744-7a8c-40bc-9968-761082e68ebd)

- **Ao clicar no roteiro escolhido você é emcaminado para a página daquele roteiro**
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/4f08a9cf-485c-4e0b-85c0-d875f1d7aa72)
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/72219b25-b14c-41a1-aaba-b86771f801b8)

- **Ao clicar no botão "Gerar roteiro através de IA"**
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/91c5e666-0cae-4045-a63c-39b5f2d70f95)

- **Página de todos os roteiros do usuário logado**
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/5eeab06b-be6c-465f-953c-87f3d3d68194)

- **Página Cadastro**
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/d5c76145-2489-4062-aadb-9b911b983e08)

- **Página Login**
  ![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/892a3d86-5260-4ab4-a771-6da265297a3e)


- **Página Sobre Nós**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/2d109555-d49d-4e83-b606-2fe7d237b196)










