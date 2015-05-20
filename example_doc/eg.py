"""Provide examples for common modules and functions (and log the requirement for the example)

Usage:
In[]: from example_doc import eg
In[]: import re  # a module we're not sure how to use
In[]: eg(re.sub)  # shows examples of usage

Project:
https://github.com/ianozsvald/ipython_example_doc"""

import inspect

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


def _get_full_name(x):
    if inspect.ismodule(x):
        #print("is a module")
        full_name = x.__name__
    if inspect.isfunction(x) or inspect.ismethod(x):
        #print("is a function")
        module = inspect.getmodule(x)
        full_name = module.__name__ + "." + x.__name__
    return full_name


examples = {
'pandas.tseries.tdi.timedelta_range': 'pandas.tseries.tdi.timedelta_range needs some help',

'pandas.from_csv': 'WE NEED THIS',

'pandas.core.generic.resample':
"""resample(rule="1D", how="sum")
rule can have the form '5Min' (minute), '2h' (hour), 'D' (day), '2D' (2 day), 'M' (month)
Common rules: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
how can use 'sum', 'mean', 'ohlc', np.max, np.mean""",

're.sub': """sub allows direct substitutions from a pattern match:
re.sub('\d+', "WASANUMBER", "stuff and 23, 55, no more")
'stuff and WASANUMBER, WASANUMBER, no more'

It also allows for more complex functions (e.g. a lambda) to be called:
re.sub('\d+', lambda match_obj: str(int(match_obj.group(0))*2), "stuff and 23, 55, no more")
'stuff and 46, 110, no more'
"""
}


def eg(mod_or_fn):
    """Provide examples for mod_or_fn if we have them & log request for examples remotely

    eg(re.sub) will print help for the re.sub module

    If an example is found we log this remotely (so we know that the example is used)
    If an example is not found we log the requrement for the example (so we know to add a new one)
    """
    # strip the path names and try to get the full module (and function) name
    full_name = _get_full_name(mod_or_fn)
    # get a matching example
    match = examples.get(full_name)
    if match:
        print(match)
    else:
        print("We don't know anything about '{}'...please Pull Request a new example at: https://github.com/ianozsvald/ipython_example_doc".format(full_name))


if __name__ == "__main__":
    print("Example usage:")
    import pandas as pd
    eg(pd.timedelta_range)

    import re
    eg(re.sub)
