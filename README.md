
# Terra Trip - Seu Guia de Viagens

Bem-vindo ao Terra Trip, seu guia de viagens personalizado! Este projeto é uma plataforma que visa fornecer informações detalhadas sobre continentes, países, cidades e pontos turísticos ao redor do mundo. 

# Sumário
1. [Sobre o Projeto](#sobre-o-projeto)

2. [Como Executar Localmente](#como-executar-o-projeto-localmente)

3. [Link do vídeo do projeto rodando](#link-do-video-do-projeto)

4. [Imagens do projeto](#imagens-do-projeto)

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

### Link do vídeo do projeto
https://www.youtube.com/watch?v=TxYkxNebk5g
### Imagens do projeto
- **Home**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/3c3f27f8-e4a8-4850-9e1c-5f81b7791a82)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/15d4f3b4-af76-462e-bc06-fef0777a601e)

- **Ao clicar no card do continente é levado para essa página dos países filtrado pelo continente selecionado**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/a5cf9268-d1af-49be-9458-e1a0b3f90d9f)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/56badaee-7d01-46f8-b4dc-8bfd7996f399)

- **Ao clicar no card do país é levado para essa página do país onde mostra as principais cidades e atrações filtrado pelo país selecionado**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/1c947a64-0f19-460a-82c0-390699161a99)
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/40734f5c-65e4-478c-8953-fc51d57f862a)

- **Página Sobre Nós**
![image](https://github.com/Leonardo-Valerio/Projeto-Terra-Trip/assets/128194207/e0a3f2ee-4ccc-4790-afd4-39e7ade8e279)







