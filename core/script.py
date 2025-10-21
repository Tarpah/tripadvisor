

from manage import *
import contextlib, io

from django.contrib.auth import get_user_model
from django.db import IntegrityError

saida = io.StringIO()

# Inicialização do django e definição das configurações
with contextlib.redirect_stdout(saida):
    main()

from decimal import Decimal
from datetime import date
from tripadvisor.models import *


def popular_tabelas():
    cat_museus = Categoria.objects.create(nome='Museus', classificacao=Classificacao.GENERAL,
                                          descricao='Espaços dedicados à arte e história.'
    )

    cat_parques = Categoria.objects.create(
        nome='Parques e Natureza',
        classificacao=Classificacao.FAMILIES,
        descricao='Áreas verdes para lazer.'
    )

    # Atração 1
    margs = Atracao.objects.create(
        nome='Museu de Arte do Rio Grande do Sul (MARGS)',
        nota=4.7,
        ingresso=True,
        valor=Decimal('20.00'),
        site='http://www.margs.rs.gov.br',
        telefone='5132272399'
    )
    margs.categorias.set([cat_museus])

    # Atração 2
    redencao = Atracao.objects.create(nome='Parque Farroupilha (Redenção)', nota=4.8, ingresso=False,
                                      site='http://www.portoalegre.rs.gov.br')
    redencao.categorias.set([cat_parques])


    # Atração 3
    ibere = Atracao.objects.create(
        nome='Fundação Iberê Camargo',
        nota=4.9,
        ingresso=True,
        valor=Decimal('30.00'),
        site='http://www.iberecamargo.org.br',
        telefone='5132478000'
    )
    ibere.categorias.set([cat_museus])

    # Perfil 1
    ana = Perfil.objects.create(
        email='ana.silva.exemplo@email.com',
        nome='Ana da Silva Sauro',
        passaporte='BR12345678',
        senha='senha_forte_da_ana',
        data_nascimento=date(1995, 10, 20),
        pais='Brasil',
        genero=Genero.WOMAN,
        lingua='Português',
        premium=True
    )

    # Perfil 2
    bruno = Perfil.objects.create(
        email='bruno.mendes.teste@email.com',
        nome='Bruno Mendes de Almeida',
        passaporte='PT87654321',
        senha='senha_do_bruno123',
        data_nascimento=date(1988, 5, 15),
        pais='Portugal',
        genero=Genero.MAN,
        lingua='Português',
        premium=False
    )

    # Perfil 3
    carla = Perfil.objects.create(
        email='carla.jones.sample@email.com',
        nome='Carla Jones Pereira',
        passaporte='US98765432',
        senha='carlapassword!',
        data_nascimento=date(2001, 2, 28),
        pais='Estados Unidos',
        genero=Genero.NOT_INFORMED,
        pagina_pessoal='https://carlajones.example.com',
        biografia='Viajante e fotógrafa amadora explorando o mundo.',
        lingua='Inglês'
    )


    # Viagem 1
    viagem_buenos_aires = Viagem.objects.create(
        titulo="Férias em Buenos Aires",
        destino="Buenos Aires",
        pais_destino="Argentina",
        orcamento=Decimal("5000.00"),
        proposito=Proposito.VACATION,
        transporte=Transporte.PLANE,
        notas="Visitar Caminito, Recoleta e comer um bom bife de chorizo.",
        perfil=carla
    )

    # Viagem 2
    viagem_sao_paulo = Viagem.objects.create(
        titulo="Conferência em São Paulo",
        descricao="Viagem de trabalho para a conferência anual de tecnologia.",
        destino="São Paulo",
        pais_destino="Brasil",
        orcamento=Decimal("2500.50"),
        proposito=Proposito.BUSINESS,
        transporte=Transporte.PLANE,
        perfil=bruno,
    )

    # Viagem 3
    viagem_patagonia = Viagem.objects.create(
        titulo="Mochilão pela Patagônia",
        pais_destino="Chile/Argentina",
        orcamento=Decimal("8000.00"),
        proposito=Proposito.BACKPACKING,
        transporte=Transporte.SEVERAL,
        perfil=ana,
    )


    # Questão 1
    questao_margs = Questao.objects.create(
        perfil=ana,
        titulo="Acessibilidade no MARGS",
        texto="Gostaria de saber se o Museu de Arte do Rio Grande do Sul possui rampas de acesso e elevadores para cadeirantes em todas as suas exposições.",
        status=Status.ANSWERED,
        likes=15
    )

    # Questão 2
    questao_redencao = Questao.objects.create(
        perfil=bruno,
        titulo="Estacionamento na Redenção aos domingos",
        texto="É fácil encontrar lugar para estacionar o carro perto do Parque Farroupilha em um domingo de manhã? Existem estacionamentos pagos nas proximidades?",
        status=Status.NOT_ANSWERED,
        likes=5
    )


    # Resposta 1
    resposta_margs = Resposta.objects.create(
        perfil=bruno,
        questao=questao_margs,
        titulo="Sim, o MARGS é bem acessível!",
        texto="Estive lá no mês passado com minha avó e confirmo que o museu tem rampas de acesso na entrada e elevadores que levam a todos os andares. A circulação interna é bem tranquila.",
        likes=22
    )

    # Resposta 2
    resposta_redencao = Resposta.objects.create(
        perfil=carla,
        questao=questao_redencao,
        titulo="Sobre estacionar no parque aos domingos",
        texto="É realmente bem complicado estacionar de graça nas ruas ao redor do parque. Minha dica é procurar os estacionamentos pagos nas ruas próximas, como a Rua da República ou a José Bonifácio.",
        likes=18
    )


    # Endereço 1
    end_margs = Endereco.objects.create(
        atracao=margs,
        cep="90010150",
        logradouro="Praça da Alfândega",
        numero=101,
        complemento="Prédio histórico no centro",
        bairro="Centro Histórico",
        cidade="Porto Alegre",
        estado="Rio Grande do Sul",
        pais="Brasil"
    )

    # Endereço 2
    end_redencao = Endereco.objects.create(
        atracao=redencao,
        cep="90050100",
        logradouro="Avenida José Bonifácio",
        numero=500,
        complemento="Parque público",
        bairro="Farroupilha",
        cidade="Porto Alegre",
        estado="Rio Grande do Sul",
        pais="Brasil"
    )

    # Endereço 3
    end_ibere = Endereco.objects.create(
        atracao=ibere,
        cep="90810240",
        logradouro="Avenida Padre Cacique",
        numero=2000,
        complemento="Prédio da Fundação",
        bairro="Cristal",
        cidade="Porto Alegre",
        estado="Rio Grande do Sul",
        pais="Brasil"
    )


    # Avaliação 1
    aval_ana_margs = Avaliacao.objects.create(
        perfil=ana,
        atracao=margs,
        titulo="Ótima exposição de arte gaúcha!",
        texto="Adorei a visita ao MARGS. A coleção permanente é fantástica e a arquitetura do prédio é um espetáculo à parte. Recomendo muito a visita a todos.",
        nota=9,
        data_visita=date(2025, 8, 15),
        likes=42
    )

    # Avaliação 2
    aval_bruno_redencao = Avaliacao.objects.create(
        perfil=bruno,
        atracao=redencao,
        titulo="Passeio relaxante no domingo de manhã",
        texto="O parque é o coração de Porto Alegre. Perfeito para caminhar, tomar um chimarrão e aproveitar o sol. O brique de domingo é uma atração imperdível para turistas.",
        nota=10,
        data_visita=date(2025, 9, 21),
        likes=88
    )

    # Avaliação 3
    aval_carla_ibere = Avaliacao.objects.create(
        perfil=carla,
        atracao=ibere,
        titulo="Arquitetura impressionante à beira do Guaíba",
        texto="Fui principalmente pela arquitetura do Álvaro Siza e não me decepcionei. O prédio por si só já é uma obra de arte. As exposições também são muito interessantes.",
        nota=10,
        data_visita=date(2025, 7, 5),
        likes=112
    )

    print("\n --- Registros Criados! ---")

def cria_super_usuario():
    User = get_user_model()
    try:
        User.objects.create_superuser(username='admin', password='admin')
        print('Superuser criado com sucesso!')
        print('username="admin", password="admin"')
    except IntegrityError:
        print('Superuser Já existe!')
        print('username="admin", password="admin"')

def excluir_registros():
    Avaliacao.objects.all().delete()
    Resposta.objects.all().delete()
    Questao.objects.all().delete()
    Endereco.objects.all().delete()
    Viagem.objects.all().delete()
    Atividade.objects.all().delete()
    Local.objects.all().delete()
    Atracao.objects.all().delete()
    Categoria.objects.all().delete()
    Perfil.objects.all().delete()

    User = get_user_model()
    User.objects.filter(is_superuser=False).delete()

    print("Registros Deletados.")

def __main__():
    flag = True
    while flag:
        print("\n== MENU ===")
        print("1. Gerar dados")
        print("2. Criar superusuário")
        print("3. Atualizar")
        print("4. Deletar registros")
        print("5. Consultar 1 único registro")
        print("6. Consultar diferentes registros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                popular_tabelas()
            case '2':
                cria_super_usuario()
            case '3':
                print('opcao_3')
            case '4':
                flag_registro = True
                while flag_registro:
                    print("1. Por Registro")
                    print("2. Todos os Registros")
                    print('0. Voltar ao menu principal')

                    opcao_registro = input("Escolha uma opção:")

                    match opcao_registro:
                        case '1':
                            print('opcao_1')
                        case '2':
                            excluir_registros()
                        case '0':
                            flag_registro = False
                        case _:
                            'Opção inválida'



            case '5':
                print('opcao_5')
            case '6':
                print('opcao_6')
            case '0':
                flag = False
            case _:
                print('Opção inválida')

    print("Fim do script.")


if __name__ == "__main__":
    __main__()
