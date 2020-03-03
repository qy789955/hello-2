import pandas as pd
a = pd.Series(data=[149.6*(10**6),1433.5*(10**6),227.9*(10**6),108.2*(10**6), 778.6*(10**6)],index=['Earth','Saturn', 'Mars','Venus', 'Jupiter'])
speed = 1.8*(10**6)
time = a/speed # a中每个data除以speed
print(time)
print(a)