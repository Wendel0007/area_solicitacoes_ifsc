from django.contrib.auth.models import User
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CreateUserTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Tempo de espera implícito
        super().setUp()

    def tearDown(self):
        self.driver.quit()
        super().tearDown()

    def test_create_user(self):
        # Navegar para a página de registro de usuário
        self.driver.get(self.live_server_url +
                        '/cadastro/action/')

        # Preencher o formulário de registro
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys('testuser')

        email_input = self.driver.find_element(By.NAME, 'email')
        email_input.send_keys('testemail@gmail.com')

        password_input = self.driver.find_element(By.NAME, 'password1')
        password_input.send_keys('testpassword')

        confirm_password_input = self.driver.find_element(
            By.NAME, 'password2')
        confirm_password_input.send_keys('testpassword')

        # Enviar o formulário
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.button_main').click()

        # Verificar se o usuário foi criado com sucesso
        self.assertTrue(User.objects.filter(username='testuser').exists())


class CadastroUsuarioTeste(TestCase):
    def test_cadastro_usuario(self):
        # Criação de um novo usuário
        user = User.objects.create_user(
            username='wendel.teste', email='wendel.teste@gmail.com', password='985236417')

        # Verificação do usuário criado
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(username='wendel.teste'), user)

        # Mostrando os dados
        print('\n -- Criou a BASE de Teste -- \n')
        print('\n -- Criando usuário -- \n')
        print('\n -- Usuário Criado -- \n')
        print('Usuário: ', user.username)
        print('Email: ', user.email)
        print('\n -- Apagando a BASE de Teste -- \n')

# classe de teste chamada CadastroUsuarioTeste, que herda da classe TestCase do Django, usada para testar funcionalidades do Django.

# Dentro dessa classe, há um método de teste chamado test_cadastro_usuario. Esse método é responsável por testar o cadastro de um novo usuário no sistema.

# Aqui está o que acontece no código passo a passo:

# Um novo usuário é criado utilizando o método create_user do objeto User.objects. Esse método cria um usuário com o nome de usuário 'wendel.teste', email 'wendel.teste@gmail.com' e senha '985236417'. O objeto user recebe o usuário recém-criado.

# É feita uma verificação para garantir que o usuário foi criado com sucesso. O método self.assertEqual é usado para comparar o valor retornado por User.objects.count() com 1, ou seja, verifica se existe exatamente um usuário registrado no sistema. Em seguida, o método self.assertEqual é usado novamente para verificar se o usuário retornado por User.objects.get(username='wendel.teste') é o mesmo que foi criado anteriormente e está armazenado na variável user.

# São exibidas algumas mensagens de impressão (print) para mostrar os dados do usuário criado. Essas mensagens servem apenas para visualizar as informações durante a execução do teste.

# Por fim, uma última mensagem de impressão é exibida indicando que a base de teste está sendo apagada.

# Em resumo, o código cria um novo usuário, verifica se ele foi criado corretamente e exibe os dados desse usuário. É um teste simples de cadastro de usuário no Django.
