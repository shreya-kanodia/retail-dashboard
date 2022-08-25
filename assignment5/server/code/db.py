
import csv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

db=SQLAlchemy()

engine = create_engine('sqlite:///data.db', echo=True)

metadata = MetaData()
# Define the table with sqlalchemy:
salaries = Table('salaries', metadata,
    Column('id',Integer, primary_key=True),
    Column('work_year',String(200)),
    Column('experience_level',String(50)),
    Column('employment_type',String(20)),
    Column('job_title',String(20)),
    Column('salary',Integer),
    Column('salary_currency',String(20)),
    Column('salaryinusd',Integer),
    Column('employee_residence',String(20)),
    Column('remote_ratio',Integer),
    Column('company_size',String(20)),

)
metadata.create_all(engine)
insert_query = salaries.insert()


with open('salaries.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    engine.execute(
        insert_query,
        [{
        "work_year": row[0],
        "experience_level": row[1],
        "employment_type": row[2],
        "job_title": row[3],
        "salary": row[4],
        "salary_currency": row[5],
        "salaryinusd": row[6],
        "employee_residence": row[7],
        "remote_ratio": row[8],
        "company_size": row[9]}
            for row in csv_reader]
    )
