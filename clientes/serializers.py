from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91234-1234 (respeitando os espaços e traço)"})
        return data




''' 
    Validação simples que funciona certeza

    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O celular deve ter 11 dígitos")
        return celular

    Com expressão regular
    def validate_celular(self, celular):
    """Verifica se o celular é valido (11 94444-4444)"""

        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo,celular) #vê se o modelo se enquadra nisso

        if not resposta:
            raise serializers.ValidationError("O celular deve ter 11 dígitos")
        return celular


    
    def validate_rg(self, rg):
        if len(rg) != 11:
            raise serializers.ValidationError("O rg deve ter 9 dígitos")
        return rg

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Nome não pode conter números.")
        return rg

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve conter 9 dígitos")
        return rg

'''
