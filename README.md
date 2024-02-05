# Sumário
1. [Sobre o Projeto](#sobre-o-projeto)

2. [Como Executar Localmente](#como-executar-o-projeto-localmente)

3. [Link do projeto no Vercel](#link-do-projeto-no-vercel)



# Terra Trip - Seu Guia de Viagens

Bem-vindo ao Terra Trip, seu guia de viagens personalizado! Este projeto é uma plataforma que visa fornecer informações detalhadas sobre continentes, países, cidades e pontos turísticos ao redor do mundo. 

## Sobre o Projeto

O Terra Trip é construído usando o framework web Django, oferecendo uma estrutura robusta e segura para fornecer informações de viagens. Aqui estão alguns dos principais recursos e componentes do projeto:

### Models

O banco de dados é composto por quatro modelos principais:

1. **Continentes**: Armazena informações sobre os continentes, incluindo nome, imagem, legenda e descrição.

2. **Paises**: Representa os países, com detalhes como nome, imagem, legenda, descrição e relação com o continente correspondente. Além disso, existem campos booleanos que indicam características especiais, como popularidade, estações recomendadas e mais.

3. **Cidades**: Contém informações sobre cidades, incluindo nome, legenda e relação com o país associado.

4. **Pontos_turisticos**: Armazena dados sobre pontos turísticos, como nome, imagens, legenda, coordenadas de latitude e longitude, e a cidade associada.

### Views

As views no arquivo `views.py` controlam a lógica de renderização das páginas HTML. Destacam-se as seguintes views:

- **index**: Apresenta a página inicial com informações sobre continentes e destaques de países em diferentes categorias.

- **continente**: Exibe informações detalhadas sobre um continente específico, incluindo países destacados em várias categorias.

- **pais**: Mostra detalhes sobre um país específico, incluindo cidades e pontos turísticos associados.

- **sobre_nos**: Apresenta uma página informativa sobre o Terra Trip e sua missão.

### Templates

Os templates em HTML, localizados no diretório `templates/home`, fornecem a estrutura visual das páginas. O uso de blocos facilita a extensão e personalização de cada página.

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

5. **Crie um Superusuário:**
python manage.py createsuperuser

6. **Execute o Servidor de Desenvolvimento:**
python manage.py runserver

7. **Acesse o Admin:**
- Vá para `http://127.0.0.1:8000/admin/` e faça login com as credenciais do superusuário.

8. **Explore o Terra Trip:**
- Acesse `http://127.0.0.1:8000/` e comece a explorar o Terra Trip!

### Link do projeto no Vercel
