from manage import *
import contextlib, io

from django.contrib.auth import get_user_model
from django.db import IntegrityError

saida = io.StringIO()

# Inicialização do django e definição das configurações
with contextlib.redirect_stdout(saida):
    main()

from decimal import Decimal
from datetime import date, datetime, time
from tripadvisor.models import *


def popular_tabelas():
    museus = Categoria.objects.create(
        nome='Museus',
        classificacao=Classificacao.GENERAL,
        descricao='Espaços dedicados à arte e história.'
    )

    parques = Categoria.objects.create(
        nome='Parques e Natureza',
        classificacao=Classificacao.FAMILIES,
        descricao='Áreas verdes para lazer.'
    )

    romantico = Categoria.objects.create(
        nome='Romântico',
        descricao='Destinos e atrações perfeitos para casais, jantares a luz de velas e luas de mel.',
        classificacao=Classificacao.GENERAL
    )

    familia = Categoria.objects.create(
        nome='Família',
        descricao='Programas divertidos e seguros para curtir com crianças e parentes de todas as idades.',
        classificacao=Classificacao.GENERAL
    )

    turne = Categoria.objects.create(
        nome='Turnê',
        descricao='Excursões guiadas e roteiros completos passando por múltiplos pontos turísticos.',
    )

    # Atração 1
    margs = Atracao.objects.create(
        nome='Museu de Arte do Rio Grande do Sul (MARGS)',
        nota=4.7,
        ingresso=True,
        valor=Decimal('20.00'),
        site='http://www.margs.rs.gov.br',
        telefone='51322723999'
    )
    margs.categorias.set([museus])

    # Atração 2
    redencao = Atracao.objects.create(nome='Parque Farroupilha (Redenção)', nota=4.8, ingresso=False,
                                      site='http://www.portoalegre.rs.gov.br')
    redencao.categorias.set([parques])


    # Atração 3
    ibere = Atracao.objects.create(
        nome='Fundação Iberê Camargo',
        nota=4.9,
        ingresso=True,
        valor=Decimal('30.00'),
        site='http://www.iberecamargo.org.br',
        telefone='51324780009'
    )
    ibere.categorias.set([museus])

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
        email='bruno.mendes.teste@email.edu.com',
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
        email='carla.jones.sample@email.edu.com',
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
    viagem_1 = Viagem.objects.create(
        titulo="Férias em Buenos Aires",
        destino="Buenos Aires",
        pais_destino="Argentina",
        orcamento=Decimal("5000.00"),
        proposito=Proposito.VACATION,
        transporte=Transporte.PLANE,
        notas="Visitar Caminito, Recoleta e comer um bom bife de chorizo.",
        perfil=carla,
    inicio = date(2023, 2, 28),
    final = date(2025, 2, 28),
    )

    # Viagem 2
    viagem_2 = Viagem.objects.create(
        titulo="Conferência em São Paulo",
        descricao="Viagem de trabalho para a conferência anual de tecnologia.",
        destino="São Paulo",
        pais_destino="Brasil",
        orcamento=Decimal("2500.50"),
        proposito=Proposito.BUSINESS,
        transporte=Transporte.PLANE,
        perfil=bruno,
        inicio=date(2025, 2, 28),
        final=date(2026, 2, 28),
    )

    # Viagem 3
    viagem_3 = Viagem.objects.create(
        titulo="Mochilão pela Patagônia",
        pais_destino="Chile/Argentina",
        orcamento=Decimal("11000.00"),
        proposito=Proposito.BACKPACKING,
        transporte=Transporte.SEVERAL,
        perfil=ana,
        inicio=date(2015, 2, 28),
        final=date(2023, 2, 28),
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
    resposta_1 = Resposta.objects.create(
        perfil=bruno,
        questao=questao_margs,
        titulo="ilusão, Sim, o MARGS é bem acessível!",
        texto="Estive lá no mês passado com minha avó e confirmo que o museu tem rampas impróprio de acesso na entrada e elevadores que levam a todos os andares. A circulação interna é bem tranquila.",
        likes=22
    )

    # Resposta 2
    resposta_2 = Resposta.objects.create(
        perfil=carla,
        questao=questao_redencao,
        titulo="Sobre estacionar no parque aos domingos, decepção.",
        texto="É realmente bem complicado estacionar de graça nas ruas ao redor do parque. Minha dica é procurar os estacionamentos pagos nas ruas próximas, como a Rua da República ou a José Bonifácio.",
        likes=18
    )


    # Endereço 1
    endereco_1 = Endereco.objects.create(
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
    endereco_2 = Endereco.objects.create(
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
    endereco_3 = Endereco.objects.create(
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
    avaliacao_1 = Avaliacao.objects.create(
        perfil=ana,
        atracao=margs,
        titulo="Ótima exposição de arte gaúcha!",
        texto="Adorei a visita ao MARGS. A coleção permanente é fantástica e a arquitetura do prédio é um espetáculo à parte. Recomendo muito a visita a todos.",
        nota=9,
        data_visita=date(2025, 8, 15),
        likes=42
    )

    # Avaliação 2
    avaliacao_2 = Avaliacao.objects.create(
        perfil=bruno,
        atracao=redencao,
        titulo="Passeio relaxante no domingo de manhã",
        texto="O parque é o coração de Porto Alegre. Perfeito para caminhar, tomar um chimarrão e aproveitar o sol. O brique de domingo é uma atração imperdível para turistas.",
        nota=10,
        data_visita=date(2025, 9, 21),
        likes=88
    )

    # Avaliação 3
    avaliacao_3 = Avaliacao.objects.create(
        perfil=carla,
        atracao=ibere,
        titulo="Arquitetura impressionante à beira do Guaíba",
        texto="Fui principalmente pela arquitetura do Álvaro Siza e não me decepcionei. O prédio por si só já é uma obra de arte. As exposições também são muito interessantes.",
        nota=10,
        data_visita=date(2025, 7, 5),
        likes=112
    )

    # 1 Local
    local_1 = Local.objects.create(
        nome='Museu de Arte Contemporânea',
        nota=4.8,
        ingresso=True,
        valor=Decimal('25.50'),
        informacoes='Um espaço dedicado à arte moderna com exposições rotativas.',
        site='https://www.mac-ficticio.com.br',
        telefone='11987654321',
        endereco=endereco_1,

        # Campos de Local
        horario_abertura=datetime(2025, 1, 1, 9, 0),  # 09:00
        horario_fechamento=datetime(2025, 1, 1, 18, 0),  # 18:00
        acessibilidade=True,
        classificao=Classificacao.GENERAL,
    )
    local_1.categorias.add(romantico)


    # 2 Local
    local_2 = Local.objects.create(
        nome='Parque das Araucárias',
        nota=4.9,
        ingresso=False,
        valor=Decimal('0.00'),
        informacoes='Área verde perfeita para piqueniques e caminhadas.',
        site='https://www.parques-cidade.gov.br',
        telefone='51912345678',
        endereco=endereco_2,

        horario_abertura=datetime(2025, 1, 1, 6, 0),  # 06:00
        horario_fechamento=datetime(2025, 1, 1, 22, 0),  # 22:00
        acessibilidade=True,
        classificao=Classificacao.GENERAL,

    )
    local_2.categorias.add(familia)

    # 3 Local
    local_3 = Local.objects.create(
        nome='Ruínas da Fortaleza Velha',
        nota=4.2,
        ingresso=True,
        valor=Decimal('12.00'),
        informacoes='Sítio arqueológico do século XVIII. Terreno irregular.',
        site='https://www.historia-local.com',
        telefone='21998765432',
        endereco=endereco_3,

        horario_abertura=datetime(2025, 1, 1, 10, 0),
        horario_fechamento=datetime(2025, 1, 1, 16, 0),
        acessibilidade=False,  # Não acessível
        classificao=Classificacao.GENERAL  # Supondo que GENERAL seja 'Livre'
    )

    # 4 Local
    local_4 = Local.objects.create(
        nome='The Blue Jazz Club',
        nota=4.7,
        ingresso=True,
        valor=Decimal('50.00'),  # Valor do Couvert/Entrada
        informacoes='Música ao vivo e drinks artesanais.',
        site='https://www.bluejazz.com',
        telefone='11955554444',
        endereco=endereco_2,

        horario_abertura=datetime(2025, 1, 1, 19, 0),  # 19:00
        horario_fechamento=datetime(2025, 1, 1, 2, 0),  # 02:00
        acessibilidade=True,
        classificao=Classificacao.GENERAL  # Ou +18 se tiver no seu Enum
    )

    # 5 Local
    local_5 = Local.objects.create(
        nome='Mega Adventure Park',
        nota=3.9,
        ingresso=True,
        valor=Decimal('150.00'),
        informacoes='Montanhas russas radicais e praça de alimentação.',
        site='https://www.megapark.com.br',
        telefone='41933332222',
        endereco=endereco_1,

        horario_abertura=datetime(2025, 1, 1, 10, 0),
        horario_fechamento=datetime(2025, 1, 1, 20, 0),
        acessibilidade=True,
        classificao=Classificacao.GENERAL
    )


    atividade_1 = Atividade.objects.create(
        nome='Trilha do Nascer do Sol',
        nota=4.9,
        ingresso=False,  # Gratuito
        valor=Decimal('120.00'),
        informacoes='Caminhada íngreme para ver o nascer do sol. Levar água.',
        site='https://www.trilhaslocais.com',
        telefone='48999998888',
        endereco=endereco_3,

        # Campos de Atividade
        turno=Turno.MORNING,
        duracao=time(3, 30),
        guia=True,
        participantes=15,
        dificuldade=Dificuldade.MEDIUM
    )


    atividade_2 = Atividade.objects.create(
        nome='Mergulho nos Corais',
        nota=4.7,
        ingresso=True,
        valor=Decimal('250.00'),
        informacoes='Inclui equipamento completo e instrutor credenciado.',
        site='https://www.mergulho-pro.com.br',
        telefone='81988887777',
        endereco=endereco_1,

        turno=Turno.AFTERNOON,
        duracao=time(2, 0),
        guia=True,
        participantes=4,
        dificuldade=Dificuldade.HARD
    )

    atividade_3 = Atividade.objects.create(
        nome='City Tour Histórico',
        nota=4.5,
        ingresso=True,
        valor=Decimal('60.00'),
        informacoes='Passeio de ônibus pelos principais pontos turísticos do centro.',
        site='https://www.turismo-cidade.com',
        telefone='11977776666',
        endereco=endereco_2,

        turno=Turno.MORNING,
        duracao=time(4, 0),
        guia=True,
        participantes=30,
        dificuldade=Dificuldade.EASY
    )


    atividade_4 = Atividade.objects.create(
        nome='Workshop de Culinária Local',
        nota=5.0,
        ingresso=True,
        valor=Decimal('120.00'),
        informacoes='Aprenda a fazer o prato típico da região e jante sua criação.',
        site='https://www.chef-local.com',
        telefone='31966665555',
        endereco=endereco_3,

        turno=Turno.NIGHT,
        duracao=time(3, 0),
        guia=True,
        participantes=10,
        dificuldade=Dificuldade.EASY
    )

    atividade_5 = Atividade.objects.create(
        nome='Expedição de Caiaque',
        nota=4.3,
        ingresso=True,
        valor=Decimal('45.00'),
        informacoes='Aluguel de caiaque duplo ou individual. Colete obrigatório.',
        site='https://www.lago-aventura.com',
        telefone='21955554444',
        endereco=endereco_1,

        turno=Turno.AFTERNOON,
        duracao=time(1, 30),
        guia=False,
        participantes=2,
        dificuldade=Dificuldade.MEDIUM
    )

    print("\n --- Registros Criados! ---")

def cria_usuarios():
    User = get_user_model()
    try:
        User.objects.create_superuser(username='ifrs', password='ifrs')
        print('Superuser criado com sucesso!')
        print('username="ifrs", password="ifrs"\n')

        User.objects.create_user(username='user', password='restinga2025')
        print('usuário user criado com sucesso!')
        print('username="user", password="restinga2025"\n')

        User.objects.create_user(username='comum', password='restinga2025')
        print('usuário comum criado com sucesso!')
        print('username="comum", password="restinga2025"\n')

    except IntegrityError:
        print('Superuser Já existe!')
        print('username="ifrs", password="ifrs"')


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

def consulta_unico_registro(opcao):

    menu_pesquisa = True
    while menu_pesquisa:
        print("\n== Escolha Model para pesquisar ===")
        print("1. Atividade")
        print("2. Atração")
        print("3. Avaliação")
        print("4. Categoria")
        print("5. Endereço")
        print("6. Local")
        print("7. Perfil")
        print("8. Questão")
        print("9. Resposta")
        print("10. Viagem")
        print("0. Voltar\n")

        opcao_escolhida = input("Digite a opção desejada:")
        if opcao_escolhida != "0":
            pk_pesquisado = int(input('Digite o pk registro desejado:'))

        consulta=False

        match opcao_escolhida:
            case "1":
                consulta = Atividade.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Atividade.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Atividade.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")


            case "2":
                consulta = Atracao.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Atracao.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Atracao.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "3":
                consulta = Avaliacao.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Avaliacao.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Avaliacao.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "4":
                consulta = Categoria.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Categoria.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Categoria.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "5":
                consulta = Endereco.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Endereco.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Endereco.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "6":
                consulta = Local.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Local.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Local.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "7":
                consulta = Perfil.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Perfil.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Perfil.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "8":
                consulta = Questao.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Questao.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")


                if opcao == "excluir":
                    objeto = Questao.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "9":
                consulta = Resposta.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Resposta.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")


                if opcao == "excluir":
                    objeto = Resposta.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case "10":
                consulta = Viagem.objects.find_by_id(pk_pesquisado)
                print(consulta)

                if opcao == "atualizar":
                    objeto = Viagem.objects.get(pk=pk_pesquisado)
                    atributo_escolhido = input("Digite o nome do atributo que será atualizado:")
                    novo_valor = input("Digite o novo valor para o atributo:")
                    setattr(objeto, atributo_escolhido, novo_valor)
                    objeto.save()
                    print("Atualizacao Concluida")

                if opcao == "excluir":
                    objeto = Viagem.objects.get(pk=pk_pesquisado)
                    objeto.delete()
                    print("Registro Excluido!")

            case _:
                menu_pesquisa = False

        if not consulta:
            menu_pesquisa = False

def consultas():
    menu_consulta = True
    while menu_consulta:
        print("\n== Escolha Model para pesquisar ===")
        print("1 (Local) Locais por cidade (case-insensitive)")
        print("2 (Local) Locais com nota média maior ou igual a 4.5")
        print("3 (Local) Locais por país em uma lista de países")
        print("4 (Local) Locais sem endereço cadastrado")
        print("5 (Local) Locais cujo site termina com '.br'")
        print("6 (Endereco) Endereços com CEP iniciando por '90' (prefixo)")
        print("7 (Atividade) Atividades por dificuldade e idioma")
        print("8 (Atividade) Atividades com preço entre 100 e 300")
        print("9 (Atividade) Atividades da categoria 'tour' com duração > 180 min")
        print("10 (Avaliacao) Avaliações do ano corrente")
        print("11 (Avaliacao) Avaliações com nota 5 e idioma Português")
        print("12 (Avaliacao) Avaliações úteis (helpful_votes) maior ou igual 10 para um local fornecido")
        print("13 (Questao) Questões abertas (status) com texto contendo “estacionamento”")
        print("14 (Resposta) Respostas de usuários que falem Português")
        print("15 (Perfil) Perfis criados no último mês")
        print("16 (Viagem) Viagens futuras com destino no Brasil")
        print("17 (Viagem) Viagens com orçamento acima de 10 mil (qualquer moeda)")
        print("18 (Local) Locais com categorias “romântico” ou “família”")
        print("19 (Local) Locais que tenham sido avaliados por usuários que tenham se cadastrado no ano de 2025")
        print("20 (Local) Locais com pelo menos 50 avaliações")
        print("21 (Local) Locais visitados e avaliados por um perfil, ordenados pelo nome")
        print("22 (Local) Locais visitados no último ano")
        print("23 (Questao) Questões sem respostas (zero respostas)")
        print("24 (Perfil) Perfis com e-mail de domínio educacional")
        print("25 (Atividade) Atividades que podem ser realizadas no RS com preço entre 100 e 500")
        print("26 (Local) Locais avaliados entre duas datas")
        print("27 (Avaliacao) Avaliações cujo título começa por “Ótimo” e tenham a nota maior ou igual a 7")
        print("28 (Local) Locais com site, mas sem telefone")
        print("29 (Resposta) Respostas que contenham as palavras 'impróprio', 'decepção' e 'ilusão'")
        print("30 (Viagem) Viagens com ao menos uma atração no país 'Brasil'")
        print("31 (Viagem) Viagens que incluem atividades de dificuldade 'Difícil'")
        print("32 (Perfil) Perfis que falam pt-BR e que tenham cadastrado pelo menos 2 questões respondidas")
        print("33 (Atividade) Atividades com o número de participantes maiores 10 e local com nota média maior ou igual a 4")
        print("34 (Perfil) Perfis que avaliaram locais da categoria 'museu'")
        print("35 (Local) Locais com avaliações em 2025 feitas por perfis premium")
        print("36 (Atracao) Fazer um ranking das Atrações ordenadas pela nota (maiores primeiro)")
        print("37 (Local) Fazer um ranking dos Locais ordenados pela nota (maiores primeiro)")
        print("38 (Atividade) Fazer um ranking das Atividades ordenados pela nota (maiores primeiro)")
        print("0. Voltar\n")

        opcao = input("Escolha um lookup:")

        match opcao:
            case "1":
                cidade = input("Digite a cidade:")
                consulta = Local.objects.find_by_cidade(cidade)
                print(consulta)

            case "2":
                nota = 4.5
                consulta = Local.objects.find_by_nota_minima(nota)
                print(consulta)

            case "3":
                pais = input("Digite o Pais:")
                consulta = Local.objects.find_by_local_pais(pais)
                print(consulta)

            case "4":
                consulta = Local.objects.find_by_no_endereco()
                print(consulta)

            case "5":
                consulta = Local.objects.find_by_site_br()
                print(consulta)

            case "6":
                consulta = Endereco.objects.find_by_cep()
                print(consulta)

            case "7":
                dificuldade = input("Digite a Dificuldade:")
                pais = input("Digite o Pais:")
                consulta = Atividade.objects.find_by_dificuldade_idioma(dificuldade, pais)
                print(consulta)

            case "8":
                consulta = Atividade.objects.find_by_preco()
                print(consulta)

            case "9":
                consulta = Atividade.objects.find_by_categoria_duracao()
                print(consulta)

            case "10":
                consulta = Avaliacao.objects.find_avaliacoes_atuais()
                print(consulta)

            case "11":
                consulta = Avaliacao.objects.find_melhores_portugues()
                print(consulta)

            case "12":
                local = input("Digite o local:")
                consulta = Avaliacao.objects.find_uteis_by_local(local)
                print(consulta)

            case "13":
                consulta = Questao.objects.find_abertas()
                print(consulta)

            case "14":
                consulta = Resposta.objects.find_by_idioma()
                print(consulta)

            case "15":
                consulta = Perfil.objects.find_novos_ultimo_mes()
                print(consulta)

            case "16":
                consulta = Viagem.objects.find_futuras_by_destino()
                print(consulta)

            case "17":
                consulta = Viagem.objects.find_by_orcamento()
                print(consulta)

            case "18":
                consulta = Local.objects.find_romantico_or_familia()
                print(consulta)

            case "19":
                consulta = Local.objects.find_avaliados_by_novos_usuarios()
                print(consulta)

            case "20":
                consulta = Local.objects.find_by_numero_avaliacoes()
                print(consulta)

            case "21":
                consulta = Local.objects.find_visitados_avaliados_by_perfil()
                print(consulta)

            case "22":
                consulta = Local.objects.find_visitados_ultimo_ano()
                print(consulta)

            case "23":
                consulta = Questao.objects.find_abertas()
                print(consulta)

            case "24":
                consulta = Perfil.objects.find_perfis_educacionais()
                print(consulta)

            case "25":
                consulta = Atividade.objects.find_atividades_estado_preco()
                print(consulta)

            case "26":
                consulta = Local.objects.find_locais_avaliados_by_datas()
                print(consulta)

            case "27":
                consulta = Avaliacao.objects.find_by_titulo_nota()
                print(consulta)

            case "28":
                consulta = Local.objects.find_contato_parcial()
                print(consulta)

            case "29":
                consulta = Resposta.objects.find_by_palavras()
                print(consulta)

            case "30":
                consulta = Viagem.objects.find_viagens_pelo_brasil()
                print(consulta)

            case "31":
                consulta = Viagem.objects.find_viagens_dificeis()
                print(consulta)

            case "32":
                consulta = Perfil.objects.find_by_idioma_questoes_respondidas()
                print(consulta)

            case "33":
                consulta = Atividade.objects.find_by_participantes_e_nota()
                print(consulta)

            case "34":
                consulta = Perfil.objects.find_by_avaliacao_museu()
                print(consulta)

            case "35":
                consulta = Local.objects.find_by_avaliacao_premium()
                print(consulta)

            case "36":
                consulta = Atracao.objects.ranking()
                print(consulta)

            case "37":
                consulta = Local.objects.ranking()
                print(consulta)

            case "38":
                consulta = Atividade.objects.ranking()
                print(consulta)

            case _:
                "Opção Inválida"
                menu_consulta = False


def __main__():
    flag = True
    while flag:
        print("\n== MENU ===")
        print("1. Gerar dados")
        print("2. Criar usuários")
        print("3. Atualizar")
        print("4. Deletar registros")
        print("5. Consultar 1 único registro")
        print("6. Consultar diferentes registros")
        print("9. Testes de consulta")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                popular_tabelas()
            case '2':
                cria_usuarios()
            case '3':
                consulta_unico_registro("atualizar")
            case '4':
                flag_registro = True
                while flag_registro:
                    print("1. Por Registro")
                    print("2. Todos os Registros")
                    print('0. Voltar ao menu principal')

                    opcao_registro = input("Escolha uma opção:")

                    match opcao_registro:
                        case '1':
                            consulta_unico_registro("excluir")
                        case '2':
                            excluir_registros()
                        case '0':
                            flag_registro = False
                        case _:
                            'Opção inválida'

            case '5':
                consulta_unico_registro("consultar")
            case '6':
                consultas()
            case '9':
                print('opção para testes')
                consulta = Atividade.objects.lookup_38()
                return print(consulta)

            case '0':
                flag = False
            case _:
                print('Opção inválida')

    print("Fim do script.")


if __name__ == "__main__":
    __main__()
