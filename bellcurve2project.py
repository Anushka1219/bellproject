import pandas as pd
import plotly.figure_factory as px
import plotly.graph_objects as go
import csv
import statistics

sd1list=[]
sd2list=[]
sd3list=[]




df=pd.read_csv("StudentsPerformance.csv")

mean=statistics.mean(df["writing score"])
sd=statistics.stdev(df["writing score"])

sd1start,sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-2*sd,mean+2*sd
sd3start,sd3end=mean-3*sd,mean+3*sd

fig=px.create_distplot([df["writing score"].tolist()],["writing score"])
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.17],mode="lines",name="sd3"))
fig.show()

print(mean)
print(sd)

for i in df["writing score"]:
    if(i>sd1start and i<sd1end):
       sd1list.append(i)

for i in df["writing score"]:
    if(i>sd2start and i<sd2end):
       sd2list.append(i)

for i in df["writing score"]:
    if(i>sd3start and i<sd3end):
       sd3list.append(i)


print(len(sd1list)*100/len(df["writing score"]))
print(len(sd2list)*100/len(df["writing score"]))
print(len(sd3list)*100/len(df["writing score"]))

    
    

