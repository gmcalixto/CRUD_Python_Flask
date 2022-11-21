# Utilizando microsserviços Flask

Exemplo de microsserviços em Flask referente a requisições HTTP manipulando um modelo de dados em SQLite.

Você pode testar direto no Replit pelo link
https://replit.com/@GustavoCalixto/CRUDPythonFlask

Enpoints implementados para testes. Entrada e sáida de dados em formato JSON
  
- /pessoas [GET]: retorna com a lista de todas as pessoas
- /pessoa/numerodoCPF [GET]</b>: retorna os dados de uma pessoa pelo CPF. Exemplo: /pessoa/12312312311
- /pessoa/numerodoCPF [DELETE]</b>: remove um CPF tendo retorno ok se removido ou not_found se o CPF não for encontrado. Exemplo: /pessoa/12312312311- 
- /pessoa [POST]: insere ou atualiza uma pessoa tendo com corpo de entrada um objeto JSON. Se o CPF mencionado for encontrado, os dados são atualizados. Senão, a nova pessoa é inserida. Exemplo:
    
```
    	{
            "nome": "José", 
            "sobrenome": "Souza",
            "CPF": "34534534577", 
            "data_nascimento": "19450312"
        }
 ```
