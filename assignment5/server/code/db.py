import sqlite3
from pathlib import Path
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
Path("data.db").touch()

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

salaries_data = pd.read_csv("./salaries.csv")

salaries_data.to_sql("salaries", connection, if_exists="replace", index=False)

connection.commit()
connection.close()
