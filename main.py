import os
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS

#from mysql
#import mysql.connector
import json

#from sqlite
import sqlite3

app = Flask(__name__)
CORS(app)


#endpoint para devolver todos as pessoas cadastradas
@app.route('/')
def home():
  return render_template('index.html')

#endpoint para devolver todos as pessoas cadastradas
@app.route('/pessoas', methods=['GET'])
def pessoas():
  
  #Connecting to sqlite
  conn = sqlite3.connect('crud.db')

  #habilita o acesso das colunas por nome
  conn.row_factory = sqlite3.Row
  
  #Creating a cursor object using the cursor() method
  cursor = conn.cursor()
  
  #Retrieving data
  cursor.execute('''SELECT nome,sobrenome,cpf,data_nascimento from pessoa''')
  
  #Fetching 1st row from the table
  result = cursor.fetchall();
  
  #Closing the connection
  conn.close()

  #devolvendo o resultado do cursor já convertido em formato JSON
  #return json.dumps(result)
  return json.dumps( [dict(ix) for ix in result] )




  
#endpoint para devolver uma pessoa por CPF
@app.route('/pessoa/<cpf>', methods=['GET','DELETE'])
def pessoaPorCPF(cpf):
  
  #Connecting to sqlite
  conn = sqlite3.connect('crud.db')

  #habilita o acesso das colunas por nome
  conn.row_factory = sqlite3.Row
  
  #Creating a cursor object using the cursor() method
  cursor = conn.cursor()


  if request.method == 'GET':
  
    #Retrieving data
    cursor.execute('''SELECT nome,sobrenome,cpf,data_nascimento from pessoa where cpf=?''',[cpf])
    
    #Fetching 1st row from the table
    result = cursor.fetchall();
  
    #Closing the connection
    conn.close()
  
    #devolvendo o resultado do cursor já convertido em formato JSON
    #return json.dumps(result)
    return json.dumps( [dict(ix) for ix in result] )
    
  elif request.method == 'DELETE':

    #Retrieving data
    cursor.execute('''SELECT nome,sobrenome,cpf,data_nascimento from pessoa''')
    
    #Fetching 1st row from the table
    result = cursor.fetchall();
  
    for valor in [dict(ix) for ix in result]:
      if valor['CPF'] == cpf:
        cursor.execute('''delete from pessoa where cpf=?''',[cpf])
        conn.commit()
        content={'delete': 'ok'}
        return jsonify(content)
        
    content={'delete': 'not_found'}
    return jsonify(content)
    
        


  

#exemplo de endpoint POST
@app.route('/pessoa',methods=['POST'])
def insereAtualizaPessoa():
  data = request.get_json()
  
  nome = data['nome']
  sobrenome = data['sobrenome']
  cpf = data['CPF']
  datanascimento = data['data_nascimento']

  #Connecting to sqlite
  conn = sqlite3.connect('crud.db')

  #habilita o acesso das colunas por nome
  conn.row_factory = sqlite3.Row
  
  #Creating a cursor object using the cursor() method
  cursor = conn.cursor()

  #Retrieving data
  cursor.execute('''SELECT nome,sobrenome,cpf,data_nascimento from pessoa''')
  
  #Fetching 1st row from the table
  result = cursor.fetchall();

  for valor in [dict(ix) for ix in result]:
    if valor['CPF'] == cpf:
      cursor.execute('''UPDATE pessoa set nome=?,sobrenome=?,data_nascimento=? where cpf=?''',[nome,sobrenome,datanascimento,cpf])
      conn.commit()
      content={'update': 'ok'}
      return jsonify(content)
      
  #Insert data
  cursor.execute('''INSERT INTO pessoa (nome,sobrenome,cpf,data_nascimento) values(?,?,?,?)''',[nome,sobrenome,cpf,datanascimento])
    
  #Commit your changes in the database
  conn.commit()
  
  #Closing the connection
  conn.close()

  content={'insert': 'ok'}
  return jsonify(content)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)