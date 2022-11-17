import sqlite3
conexao=sqlite3.connect("dc_universe.db")
cursor = conexao.cursor()

#4o. passo:comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (13,'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo: Executar o comando SQL
cursor.execute(sql)

#6o. passo: confirmar o INSERT com comit() e fechar o banco
conexao.commit()
conexao.close()