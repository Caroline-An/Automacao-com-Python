#Projeto de Automação de Tarefas com Python

A atividade de aprendizagem envolveu diversas ações para lidar com as bibliotecas pandas, time e pyautogui.

O projeto foi realizado seguindo as diretivas da primeira aula gratuita de Python realizada no dia 04/03/2024 no canal [https://](https://www.youtube.com/@HashtagProgramacao)https://www.youtube.com/@HashtagProgramacao.
O objetivo consiste em  
-  fazer com que o programa abra um navegador
-  digite a URL do site utilizado para teste
-  pressione a tecla ENTER
-  faça login
-  e por fim, cadastre no sistema os produtos da base de dados fornecida para o teste

Antes de iniciar as atividades foi preciso instalar as bibliotecas, este processo foi realizado no terminal com o comando:
pip install pyautogui 
Essa instalação já trás consigo as bibliotecas pyautogui e time.

Também será utilizada a biblioteca pandas posteriormente, por tanto é necessário fazer sua instalação também com o comando:
pip install pandas numpy openpyxl

Os processos foram realizados utilizando estruturas de repetição e funções inerentes às bibliotecas importadas, como a leitura da base de dados utilizando pd.read_csv("database.csv"), a clicagem em botões com pyautogui.press("win"), write("") e click(x=000, y=000), e a otimização de tempo com as funções pyautogui.PAUSE = 1, e time.sleep(3).

Foi utilizado um arquivo chamado "auxiliador.py" para capturar a localização de onde deveria ser clicado para iniciar a preencher os dados de login, vale mencionar que não há uma autenticação de fato nesta etapa, o login é apenas para fins de realizar o teste de automação, então os dados podem ser trocados por quaiquer informações que o dev desejar.

O resultado pode ser viasualizado nos screenshots abaixo e seguindo os passos indicados nos arquivos "praticando.py".
