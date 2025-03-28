# Backend
Seleção Labens 2024 - Desafio Backend

## Execução

1. Criar o Ambiente Virtual
Primeiro, crie o ambiente virtual dentro do diretório do seu projeto.

~~~
python -m venv nome_da_venv
~~~

Substitua nome_da_venv pelo nome que deseja dar ao seu ambiente virtual.

2. Ativar o Ambiente Virtual
A ativação depende do seu sistema operacional:

No Windows:
Para ativar o ambiente virtual, use o seguinte comando:

~~~
.\nome_da_venv\Scripts\activate
~~~

No macOS/Linux:
No terminal, use:

~~~

source nome_da_venv/bin/activate

~~~

3. Verificar se a Venv foi Ativada
Após ativar o ambiente, você deve ver o nome da venv no prompt, algo como:

~~~

(nome_da_venv) user@computer:~/projeto$

~~~

Isso significa que o ambiente virtual foi ativado corretamente.

4. Povoar o banco de dados

~~~
python manage.py create_fake_tarefas
~~~

5. Executar o servidor

~~~
python3 manage.py runserver
~~~

6. End points

- http://127.0.0.1:8000/api/data/

- http://127.0.0.1:8000/api/buscar/

- http://127.0.0.1:8000/api/data/?id=[int]

- http://127.0.0.1:8000/admin

- http://127.0.0.1:8000/api

- http://127.0.0.1:8000/api/tarefa/<str:titulo_tarefa>

7. Insomnia

- POST 

Url | http://127.0.0.1:8000/api/data/ 

Body  {

	"tarefa_titulo": "< str >",

	"tarefa_descricao": "< str >",

	"tarefa_prazo": "< date >",

	"tarefa_dataConclusao": "< date >",

	"tarefa_situacao": "< enum >"
}

- DELETE

Url | http://127.0.0.1:8000/api/data/

Body | {
		"id": < int >
	}

- PATCH

URL | http://127.0.0.1:8000/api/tarefa/<str:titulo_tarefa>

body | 
{
	"tarefa_titulo": "Teste3",

	"tarefa_descricao": "Devera ser excluido",

	"tarefa_prazo": "2025-03-28",

	"tarefa_dataConclusao": "2025-03-28",

	"tarefa_situacao": "Nova"
}

- GET

URL | http://127.0.0.1:8000/api

8. Desativar o Ambiente Virtual
Quando terminar, pode desativar a venv com o comando:

~~~
deactivate
~~~

o PUT não altera a primary key, caso tente, ele ira criar um novo objeto.