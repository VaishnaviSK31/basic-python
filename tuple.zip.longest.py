from itertools import zip_longest
names=["Kohli","Rohit","Pandya","Dhoni"]
runs=[10000,9000,8000,7000]
country=["IND","IND","IND","IND"]
ipl_t=["RCB","MI"]
info=list(zip_longest(names,runs,country,ipl_t,fillvalue="#"))
print(info)