from datetime import date
import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["average"].tolist()
population_mean=statistics.mean(data)
fig=ff.create_distplot([data],['average'],show_hist=False)
fig.show()

def random_set_of_mean(counter):
    data = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        data.append(value)
    mean = statistics.mean(data)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


