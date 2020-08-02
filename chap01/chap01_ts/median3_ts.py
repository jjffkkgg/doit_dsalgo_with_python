#%%
def median_ts(a,b,c):
    median = a
    if a > b:
        if b > c:
            median = b
        else:
            if c < a:
                median = c
            else:
                median = a
    else:
        if b > c:
            if c < a:
                median = a
            else:
                median = c
        else:
            median = b
    return median
#%%
print(median_ts(1,2,3))