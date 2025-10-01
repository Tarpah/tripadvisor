from django.core.management.base import BaseCommand
from ._scripts.popular_banco import popular_banco, cria_super_usuario, excluir_registros

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('--- Menu ---')

        while True:
            print('\n===== Opções =====')
            print('1 - Popula Banco')
            print('2 - Cria super usuário admin')
            print('4 - Exclui todos os registros')
            print('0 - Sair')

            escolha = int(input('\nDigite a opção: '))

            match escolha:
                case 1:
                    popular_banco()
                case 2:
                    cria_super_usuario()
                case 4:
                    excluir_registros()
                case 0:
                    break