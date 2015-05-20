
# pd.__name__ == 'pandas'

#In [13]: inspect.getfile(pd)
#Out[13]: '/home/ian/anaconda/envs/scratch/lib/python3.4/site-packages/pandas/__init__.py'

#In [14]: inspect.getfile(pd.timedelta_range)
#Out[14]: '/home/ian/anaconda/envs/scratch/lib/python3.4/site-packages/pandas/tseries/tdi.py'

# Notifications could be sent to
# http://ianozsvald.com/ipython_example?q=blah.blob

    # might these be useful?
    #source_file_path = inspect.getsourcefile(x)
    #file_parts = split_into_file_parts(source_file_path)
    #print(file_parts)
    #possible_matches = propose_matches(file_parts)
    #print(possible_matches)

#def split_into_file_parts(filepath):
    #file_parts = filepath.split("/")  # *nix only
    #file_parts = [fp for fp in file_parts if len(fp)]
    #return file_parts


#def propose_matches(file_parts):
    #"""Combine a few file_parts to propose things to match against"""
    ## possibly we should like for site-packages as an early cut-off point?
    #matches = []
    #if len(file_parts) > 2:
        #matches.append(file_parts[-3:])
    #if len(file_parts) > 1:
        #matches.append(file_parts[-2:])
    #if len(file_parts) > 0:
        #matches.append(file_parts[-1:])
    #return matches
