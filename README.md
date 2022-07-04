# Documentação Carford

Para rodar a aplicação é necesário ter ```docker``` e ```docker-compose``` instalados em sua maquina.

 Caso já tenha os dois, basta rodar o comando ```sudo docker-compose up -d```, após isso veja qual o id do container carford_app e rode comando ```sudo docker exec -i -t idContainerCarford /bin/bash``` e agora para persistir as tabelas no banco de dados rode ```flask db upgrade```

## Visão geral:
<br>

A Carford é uma plataforma que propõe a integrar carros a seus proprietários.
Um proprietário que não possui o limite de carros é marcado como uma oportunidade, limite de três carros por pessoa.

Para registrar o carro ele deve ter uma dessas três cores, ‘yellow’, ‘blue’ or ‘gray’. E um desses modelos ‘hatch’, ‘sedan’ or ‘convertible’. 

Um carro apenas pode existir no sistema caso tenha um proprietário

<br>

- **Endpoints em Owners**:
    - **POST -  /owners**
        
        Chave cnh uma string com apenas números e ter um tamanho de 11 dígitos
        
        | CHAVES | VALORES | OBRIGATORIEDADE |
        | --- | --- | --- |
        | name | string, max(255) | X |
        | cnh | string, max(11) | X |
        
        **Requisição correta:**
        
        ```json
        {
        	"cnh": "12345678998",
        	"name": "John doe"
        }
        ```
        
        **Resposta:**
        
        ```json
        RESPONSE 201 - CREATED
        {
        	"owner_id": 1,
        	"cnh": "12345678998",
        	"name": "John Doe",
        	"opportunity": true,
        	"cars": []
        }
        ```

        <br>

        **Requisição incorreta →** Envio de cnh já existente:
        
        ```json
        {
        	"cnh": "12345678998",
        	"name": "John doe"
        }
        ```
        
         **Resposta:**
        
        ```json
        RESPONSE 409 - CONFLICT
        {
        	"error": "cnh already exists"
        }
        ```
		
		<br>
        
        **Requisição incorreta →** Envio de cnh com letras:
        
        ```json
        {
        	"cnh": "1234567899b",
        	"name": "John doe"
        }
        ```
        
        **Resposta:**
        
        ```json
        RESPONSE 422 - UNPROCESSABLE ENTITY
        {
        	"error": "cnh already exists"
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio de cnh maior ou menor que 11:
        
        ```json
        {
        	"cnh": "123",
        	"name": "John doe"
        }
        ```
        
        **Resposta:**
        
        ```json
        RESPONSE 422 - UNPROCESSABLE ENTITY
        {
        	"error": "cnh must contain 11 digits"
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio faltando alguma chave:
        
        ```json
        {
        	"name": "John doe"
        }
        ```
        
        **Resposta** → Uma lista com as chaves que faltam:
        
        ```json
        RESPONSE 400 - BAD REQUEST
        {
        	"missing_key": [
        		"cnh"
        	]
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio de chave incorreta:
        
        ```json
        {
        	"hnc": "12345678998",
        	"name": "John doe"
        }
        ```
        
        **Resposta** → Uma lista com as chaves corretas e outra com as chaves enviadas erradas:
        
        ```json
        RESPONSE 400 - BAD REQUEST
        {
        	"error": "invalid keys",
        		"expected_keys": [
        			"cnh",
        			"name"
        		],
        		"received_key": [
        			"hnc"
        	]
        }
        ```

		<br>
        
    - **GET - /owners**
        
        Não tem corpo na requisição.
        
        **Resposta:**
        
        ```json
        RESPONSE 201 - 
        [
        	{
        		"owner_id": 1,
        		"cnh": "12345678998",
        		"name": "John Doe",
        		"opportunity": true,
        		"cars": []
        	},
        	{
        		"owner_id": 2,
        		"cnh": "12345678999",
        		"name": "Doe John",
        		"opportunity": true,
        		"cars": [
        			{
        				"car_id": 1,
        				"color": "gray",
        				"model": "convertible",
        				"owner_id": 2
        			}
        		]
        	},
        	{
        		"owner_id": 3,
        		"cnh": "12345678988",
        		"name": "Bob",
        		"opportunity": false,
        		"cars": [
        			{
        				"car_id": 2,
        				"color": "gray",
        				"model": "convertible",
        				"owner_id": 3
        			},
        			{
        				"car_id": 3,
        				"color": "blue",
        				"model": "sedan",
        				"owner_id": 3
        			},
        			{
        				"car_id": 4,
        				"color": "yellow",
        				"model": "hatch",
        				"owner_id": 3
        			}
        		]
        	}
        ]
        ```
        
    - **GET OPPORTUNITIES - /owners/opportunities**
        
        Não tem corpo na requisição.
        
        Retorna apenas owners são uma oportunidade
        
        ```json
        RESPONSE 201 - 
        [
        	{
        		"owner_id": 1,
        		"cnh": "12345678998",
        		"name": "John Doe",
        		"opportunity": true,
        		"cars": []
        	},
        	{
        		"owner_id": 2,
        		"cnh": "12345678999",
        		"name": "Doe John",
        		"opportunity": true,
        		"cars": [
        			{
        				"car_id": 1,
        				"color": "gray",
        				"model": "convertible",
        				"owner_id": 2
        			}
        		]
        	}
        ]
        ```
        
    - **PATCH - /owners/<owner_id>**
        
        Chaves que podem ser alteradas são “name” e “cnh”
        
        As regras de chave incorreta ou faltando é a mesma de post - /owners
        
        Não é possível alterar a cnh para uma que já existe no banco de dados
        
        **Requisição correta:** 
        
        ```json
        {
        	"name": "kenny"
        }
        ```
        
        **Resposta:**
        
        ```json
        RESPONSE 200 - OK
        {
        	"owner_id": 1,
        	"cnh": "12345678998",
        	"name": "Kenny",
        	"opportunity": true,
        	"cars": []
        }
        ```
        
    
- **Endpoints em Cars**:
    - **POST -  /cars**
        
        Ao número de carros de um usuário chegar a três a chave “opportunity” se torna false e não é mais possível vincular um carro para este “owner”
        
        | CHAVES | VALORES | OBRIGATORIEDADE |
        | --- | --- | --- |
        | color | string, max(6) | X |
        | model | string, max(11) | X |
        | owner_id | integer | X |
        
        **Requisição correta:**
        
        ```json
        {
        	"color": "gray",
        	"model": "convertible",
        	"owner_id": 2
        }
        ```
        
        **Resposta:**
        
        ```json
        RESPONSE 201 - CREATED
        {
        	"car_id": 1,
        	"color": "gray",
        	"model": "convertible",
        	"owner_id": 2
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio de “owner_id” não existente:
        
        ```json
        {
        	"color": "Gray",
        	"model": "Convertible",
        	"owner_id": 100
        }
        ```
        
         **Resposta:**
        
        ```json
        RESPONSE 404 - NOT FOUND
        {
        	"error": "owner_id not found"
        }
        ```

		<br>
        
        **Requisição incorreta →** Enviando um novo carro para “owner” com limite:
        
        ```json
        {
        	"color": "gray",
        	"model": "convertible",
        	"owner_id": 3
        }
        ```
        
         **Resposta:**
        
        ```json
        RESPONSE 409 - CONFLICT
        {
        	"error": "This owner already has the car limit"
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio de “color” diferente da permitida:
        
        ```json
        {
        	"color": "red",
        	"model": "convertible",
        	"owner_id": 2
        }
        ```
        
        **Resposta →** Uma lista com as “colors” permitidas
        
        ```json
        RESPONSE 422 - UNPROCESSABLE ENTITY
        {
        	"error": "invalid color value",
        	"expected_color": [
        		"yellow",
        		"blue",
        		"gray"
        	]
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio de “model” diferente da permitida:
        
        ```json
        {
        	"color": "gray",
        	"model": "SUV",
        	"owner_id": 2
        }
        ```
        
        **Resposta →** Uma lista com as “models” permitidas
        
        ```json
        RESPONSE 422 - UNPROCESSABLE ENTITY
        {
        	"error": "invalid model value",
        	"expected_model": [
        		"hatch",
        		"sedan",
        		"convertible"
        	]
        }
        ```

		<br>
        
        **Requisição incorreta →** Envio faltando alguma chave:
        
        ```json
        {
        	"owner_id": 2
        }
        ```
        
        **Resposta** → Uma lista com as chaves que faltam:
        
        ```json
        RESPONSE 400 - BAD REQUEST
        {
        	"missing_key": [
        		"color",
        		"model"
        	]
        }
        ```
        
		<br>

        **Requisição incorreta →** Envio de chave incorreta:
        
        ```json
        {
        	"cores": "gray",
        	"modelos": "SUV",
        	"owner_id": 2
        }
        ```
        
        **Resposta** → Uma lista com as chaves corretas e outra com as chaves enviadas erradas:
        
        ```json
        RESPONSE 400 - BAD REQUEST
        {
        	"error": "invalid keys",
        	"expected_keys": [
        		"color",
        		"model",
        		"owner_id"
        	],
        	"received_key": [
        		"cores",
        		"modelos"
        	]}
        ```
		
		<br>
        
    - **DELETE - /cars/<car_id>**
        
        Não tem corpo na requisição
        
        Caso o carro deletado seja de um “owner” que tenha três carros, a chave “opportunity” será alterada para true novamente.
        
        **Requisição correta →Retorna:**
        
        ```json
        RESPONSE 204 - NO CONTENT
        ```
        
		<br>
		
        **Requisição incorreta →car_id não existe → Retorna:**
        
        ```json
        RESPONSE 400 - NOT FOUND
        {
        	"error": "car_id not found"
        }
        ```