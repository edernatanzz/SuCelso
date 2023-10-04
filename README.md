# SuCelso-Student-Management-System

passo a passo para executar o projeto :(COMANDOS PARA EXECUTAR NO TERMINAL DO VSCODE ! )


1-instale o python e django : pip install python em seguida pip install django 


2- va em setings e exclua a data base existente e use a de teste tirando os '#' das linhas


3-faça a migração dos models do banco de dados agora com comandos python manage.py makemigrations e python manage.py migrate 


4- crie um super usuario para logar no projeto : python manage.py createsuperuser coloque o email,usuario , senha e y.


5-agora feito tudo isso execute o projeto com python manage.py runserver.
vai dar um erro devido a importação do mysql que estava usando e foi removido , então exlua a linha em que o erro aparece (setings, linha 16 e delete)


6- com o projeto executado vá em qualquer navegador e pode colocar essse endereço - 127.0.0.1:8000/

arquivo da documentação -Documento de requisitos : [Requisitos Funcionais Escola-SuCelso.docx.pdf](https://github.com/edernatanzz/SuCelso/files/12798147/Requisitos.Funcionais.Escola-SuCelso.docx.pdf)


