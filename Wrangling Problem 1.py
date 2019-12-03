import pandas as pd

We = {'Student': ['Ice Bear','Panda','Grizzly'],'Math': [80,95,79]}
We = pd.DataFrame(We, columns = ['Student','Math'])

Are = {'Student': ['Ice Bear','Panda','Grizzly'],'Electronics': [85,81,83]}
Are = pd.DataFrame(Are, columns = ['Student','Electronics'])

Your = {'Student': ['Ice Bear','Panda','Grizzly'],'GEAS': [90,79,93]}
Your = pd.DataFrame(Your, columns = ['Student','GEAS'])

Cute = {'Student': ['Ice Bear','Panda','Grizzly'],'ESAT': [93,89,88]}
Cute = pd.DataFrame(Cute, columns = ['Student','ESAT'])

Bare = pd.merge(We, Are, how = 'outer', on = 'Student')

Bears = pd.merge(Bare, Your, how = 'outer', on = 'Student')

print (" ")
print(pd.merge(Bears, Cute, how = 'outer', on = 'Student'))
print (" ")
longformat = pd.melt(Bow, id_vars = 'Student', value_vars =['Math','Electronics','GEAS', 'ESAT'])

print(longformat.rename(columns = {'variable':'Subject','value': 'Grades'}))