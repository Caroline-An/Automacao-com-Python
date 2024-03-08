# Projeto de Automação de Tarefas com Python

A atividade de aprendizagem envolveu diversas ações para lidar com as bibliotecas *__pandas, time e pyautogui__*.

O projeto foi realizado seguindo as diretivas da primeira aula gratuita de Python realizada no dia 04/03/2024 no canal [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao).
O objetivo consiste em:
-  fazer com que o programa abra um navegador;
-  digite a URL do site utilizado para teste;
-  pressione a tecla ENTER;
-  faça login;
-  e por fim, cadastre no sistema os produtos da base de dados fornecida para o teste.

## Pré-code
Antes de iniciar as atividades foi preciso instalar as bibliotecas, este processo foi realizado no terminal com o comando:
*__pip install pyautogui__*
Essa instalação já trás consigo as bibliotecas *__pyautogui__* e *__time__*.

Também foi utilizada a biblioteca *__pandas__* posteriormente, por tanto é necessário fazer sua instalação também com o comando:
*__pip install pandas numpy openpyxl__*

## Codificando
Os processos foram realizados utilizando estruturas de repetição e funções inerentes às bibliotecas importadas, como a leitura da base de dados utilizando *__pd.read_csv("database.csv")__*, a clicagem em botões com *__pyautogui.press("win")__*, *__write("")__* e *__click(x=000, y=000)__*, e a otimização de tempo com as funções *__pyautogui.PAUSE = 1__*, e *__time.sleep(3)__*.

Foi utilizado um arquivo chamado **"auxiliador.py"** para capturar a localização de onde deveria ser clicado para iniciar a preencher os dados de login, vale mencionar que não há uma autenticação de fato nesta etapa, o login é apenas para fins de realizar o teste de automação, então os dados podem ser trocados por quaisquer informações que o dev desejar.

## Resultado
O resultado foi o cadastro eficaz no sistema de todos os dados pertencentes à base de dados em formato .csv.
