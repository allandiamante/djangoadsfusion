from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy



class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome' : 'Juliano Roberto',
            'email' : 'julinho@gmail.com',
            'assunto' : 'Assunto top sobre TI',
            'mensagem' : 'Uma mensagem de alerta para qm trabalha com TI',
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data = self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados_invalido = {
            'nome' : 'Juliano Roberto',
            'assunto' : 'Assunto top sobre TI'
        }
        request = self.cliente.post(reverse_lazy('index'), data = dados_invalido)
        self.assertEquals(request.status_code, 200)