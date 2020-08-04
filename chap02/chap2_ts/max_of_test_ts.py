#%%
from max_ts import max_of_ts as mx
#%%
t = (4,7,6,2.3,4.67,1)
s = "string"
a = ["DTS","AAC","FLAC"]

print(f"{t} 최대: {mx(t)}")
print(f"{s} 최대: {mx(s)}")
print(f"{a} 최대: {mx(a)}")