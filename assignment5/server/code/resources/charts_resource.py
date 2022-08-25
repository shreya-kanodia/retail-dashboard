
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
from flask_jwt_extended import jwt_required
from flask_restful import Resource


class BarChartOne(Resource):
    df=pd.read_csv('Data Science Jobs Salaries.csv')
    @jwt_required()
    def get(self):
        arr = np.array(self.df.groupby('experience_level').salary.median())
        y=[]
        for i in arr:
            y.append(i)

        exp_lev = ['EN','EX','MI','SE']
        print(type(exp_lev))
        return {"x":exp_lev,"y":y}

class BarChartTwo(Resource):
    df=pd.read_csv('Data Science Jobs Salaries.csv')
    @jwt_required()
    def get(self):
        res = self.df.groupby('employee_residence').salary_in_usd.mean().sort_values(ascending=False)
        res = res.head()
        return {"x":list(res.index),"y":list(res.values)}

class PieChartOne(Resource):
    df=pd.read_csv('Data Science Jobs Salaries.csv')
    @jwt_required()
    def get(self):
        coms = np.array(self.df['company_size'].value_counts(sort=True))
        print(coms)
        y=[]
        for i in coms:
            print(type(float(i)))
            y.append(float(i))
        Labels = ['L','S','M']
        print(Labels)
        data=[]
        for i in range(3):
            data.append({'value':y[i],'name':Labels[i]})
        return {"x":data}


class PieChartTwo(Resource):
    df=pd.read_csv('Data Science Jobs Salaries.csv')
    @jwt_required()
    def get(self):
        remo = np.array(self.df['remote_ratio'].value_counts(sort=True))
        y=[]
        for i in remo:
            print(type(float(i)))
            y.append(float(i))
        labels = ['Full remote', 'Partial remote', 'No remote']
        data=[]
        for i in range(3):
            data.append({'value':y[i],'name':labels[i]})
        return {"x":data}



