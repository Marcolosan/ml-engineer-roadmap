import duckdb

con = duckdb.connect()

con.execute("""
CREATE TABLE experiments (

id INTEGER,

loss_function VARCHAR,

mae FLOAT,

rmse FLOAT,

training_time INTEGER

)

""")

con.execute("""

INSERT INTO experiments VALUES

(1,'MSE',0.22,0.31,120),

(2,'Huber',0.18,0.28,150),

(3,'MAE',0.25,0.33,95),

(4,'LogCosh',0.17,0.27,160)

""")

resultado = con.execute("""

SELECT *

FROM experiments

""").fetchdf()

print(resultado)
