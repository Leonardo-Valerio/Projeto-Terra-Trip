from django.shortcuts import render, redirect, get_object_or_404
from apps.roteiros.forms import RoteiroForms, GerarRoteiroForm
from apps.roteiros.models import Roteiro
from apps.home.models import Paises
from django.contrib import messages
from django.urls import reverse
import openai
import os
import dotenv
import tiktoken
import time



def roteiros(request, roteiro_id, pais_id=None):
    if not request.user.is_authenticated:
        messages.error(request,"Para acessar essa página é necessário você fazer seu login")
        return redirect('login')
    pais = None
    roteiro = get_object_or_404(Roteiro,pk=roteiro_id)
    if pais_id is not None:
        pais = get_object_or_404(Paises,pk=pais_id)   
    if pais is not None:
        for item in roteiro.grupo_paises:
            if item["nome"] == pais.nome:
                break
        else:
            roteiro.grupo_paises.append({"id":pais_id,"nome":pais.nome,"imagem":pais.imagem.url})
            roteiro.save()

    gerar_roteiro_form = GerarRoteiroForm(request.POST or None)
    if gerar_roteiro_form.is_valid():
        roteiro = get_object_or_404(Roteiro, pk=roteiro_id)
        

        prompt_user = [item["nome"] for item in roteiro.grupo_paises]
        dotenv.load_dotenv()
        openai.api_key = os.getenv("API_OPENAI_KEY")

        prompt_sistema = f"""
            Gere um roteiro de viagem com base nos seguintes critérios: países desejados, dias disponíveis e estação do ano. Leve em consideração a logística, priorizando destinos próximos para otimizar deslocamentos. Adapte as recomendações de pontos turísticos de acordo com a estação.

            *Detalhes:*
            * Países desejados: {roteiro.grupo_paises}
            * Dias disponíveis: {roteiro.dias}
            * Estação do ano: {roteiro.epoca}

            *Regras:*
            1. Se os países incluírem destinos geograficamente próximos, organize e ordene a lista de paises que receber em uma ordem lógistica para o roteiro de acordo com essa proximidade.

            2. Considere a estação do ano para adaptar as recomendações de pontos turísticos (indicar praias no verão).

            3. SOMENTE quando a distância entre um país para o outro for superior a 3 mil km, crie um roteiro separado para cada país, utilizando o período designado para cada um.

            4. Se o tempo disponível for insuficiente para todos os destinos, apresente uma versão mais condensada do roteiro para uma experiência de viagem melhor.

            *Exemplo:*
            * Países desejados: Brasil, Portugal, Argentina, Espanha
            * Dias disponíveis: 20 dias
            * Estação do ano: Verão

            *Resultado Esperado do exemplo:*
            Explicação: Tive que separar os paises em roteiros diferentes pela logica de logistica para ter uma viagem com mais sentido de rota
            Roteiro para Brasil e Argentina(20 dias)
            1. Brasil  (10 dias): [Explicação detalhada de Recomendações detalhadas para pontos turísticos no verão]
            2. Argentina (10 dias): [Explicação detalhada de Recomendações para pontos turísticos no verão]
            Roteiro para Portugal e Espanha(20 dias)
            1. Portugal  (10 dias): [Explicação detalhada de Recomendações detalhadas para pontos turísticos no verão]
            2. Espanha (10 dias): [Explicação detalhada de Recomendações detalhadas para pontos turísticos no verão]

        """

        tentativas = 0
        tempo_exponencial = 5
        modelo = "gpt-3.5-turbo"
        codificador = tiktoken.encoding_for_model(modelo)
        lista_de_tokens = codificador.encode(prompt_sistema + ' '.join(prompt_user))
        tokens = len(lista_de_tokens)
        tamanho_esperado_saida = 2048
        if tokens > (4096 - tamanho_esperado_saida):
            modelo = "gpt-3.5-turbo-16k"
        while tentativas < 5:
            try:
                tentativas += 1
                response = openai.ChatCompletion.create(
                    model=modelo,
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": "\n".join(prompt_user)}
                    ],
                    temperature=1,
                    max_tokens=tamanho_esperado_saida,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                resposta = response.choices[0].message.content
                roteiro.roteiro_gerado = resposta
                roteiro.save()
            except openai.error.AuthenticationError as e:
                print(f'ERRO DE AUTENTICAÇÃO: {e}')
            except openai.APIError as e:
                print(f'ERRO DE API: {e}')
                time.sleep(5)
            except openai.error.RateLimitError as e:
                print(f'ERRO LIMITE DE TAXA: {e}')
                time.sleep(tempo_exponencial)
                tempo_exponencial *= 2

    return render(request, 'roteiros/roteiros.html', {'pais':pais, 'roteiro':roteiro, 'gerar_roteiro_form':gerar_roteiro_form})

def todos_os_roteiros(request):
    if not request.user.is_authenticated:
        messages.error(request,"Para acessar essa página é necessário você fazer seu login")
        return redirect('login')
    roteiros = Roteiro.objects.filter(usuario_roteiro=request.user)
    form_roteiro = RoteiroForms()
    if request.method == 'POST':
        form_roteiro = RoteiroForms(request.POST)
        if form_roteiro.is_valid():
            roteiro = form_roteiro.save(commit=False)
            roteiro.usuario_roteiro = request.user
            roteiro.save()
    
    return render(request, 'roteiros/todos-roteiros.html',{'roteiros':roteiros,'form_roteiro':RoteiroForms})

def editar_roteiro(request, roteiro_id):
    roteiro = Roteiro.objects.get(id=roteiro_id)
    formulario_edit = RoteiroForms(instance=roteiro)
    if request.method == 'POST':
        formulario_edit = RoteiroForms(request.POST,instance=roteiro)
        if formulario_edit.is_valid():
            roteiro = formulario_edit.save(commit=False)
            roteiro.usuario_roteiro = request.user
            roteiro.save()
            return redirect('todos_roteiros')
    return render(request,'roteiros/editar_roteiro.html', {'form_roteiro': formulario_edit, 'roteiro_id':roteiro_id})

def deletar_roteiro(request, roteiro_id):
    roteiro = Roteiro.objects.get(id=roteiro_id)
    roteiro.delete()
    return redirect('todos_roteiros')

def remover_pais_roteiro(request, pais_id, roteiro_id):
    roteiro = Roteiro.objects.get(id=roteiro_id)
    novo_roteiro = []
    for pais in roteiro.grupo_paises:
        if pais['id'] != pais_id:
            novo_roteiro.append(pais)
    
    roteiro.grupo_paises = novo_roteiro
    roteiro.save()
    return redirect(reverse('roteiros', kwargs={'roteiro_id': roteiro_id}))