"""Provide examples for common modules and functions (and log the requirement for the example)

Usage:
In[]: from example_doc import eg
In[]: import re  # a module we're not sure how to use
In[]: eg(re.sub)  # shows examples of usage

Project:
https://github.com/ianozsvald/ipython_example_doc"""

import inspect
from urllib.request import urlopen, URLError
from socket import timeout

ALLOW_LOGGING = True  # Set to False if urlopen logging is slow for you
URLOPEN_TIMEOUT = 1.0  # seconds to wait before timing out the logging
SHOW_DEBUG_INFO = False  # Used by Ian when debugging


def log_usage(match, success):
    """Call out to logging site to note that we had an example (or not)"""
    if ALLOW_LOGGING:
        URL = "http://ianozsvald.com/ipython_example_doc?q={match}&success={success}"
        url = URL.format(match=match, success=success)
        # call the url to log whether we've provided a useful example, timeout to
        # avoid hanging
        try:
            if SHOW_DEBUG_INFO:
                print("logging to:", url)
            urlopen(url, timeout=URLOPEN_TIMEOUT)
            if SHOW_DEBUG_INFO:
                print("logged ok")
        except URLError as err:
            # note that err.code==404 means that the logging url isn't found,
            # that's totally right for my blog (as there's no such URL) but Google
            # Analytics is logging the call for my stats
            if err.code not in set([404]):
                if SHOW_DEBUG_INFO:
                    print("FAILED TO LOG (URLError)", err.code)
        except timeout:
            if SHOW_DEBUG_INFO:
                print("FAILED TO LOG (timeout)")


def _get_full_name(x):
    if inspect.ismodule(x):
        full_name = x.__name__
    if inspect.isfunction(x) or inspect.ismethod(x):
        module = inspect.getmodule(x)
        full_name = module.__name__ + "." + x.__name__
    return full_name


# NOTE deliberate violation of PEP8 with the left formatting, I expect to break
# the help out into text files later and for now this is easier on the eye (so
# please don't PEP8-it as I'll just undo it)
examples = {
#'pandas.tseries.tdi.timedelta_range': 'pandas.tseries.tdi.timedelta_range needs some help',

#'pandas.from_csv': 'WE NEED THIS',

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


def eg(mod_or_fn=None):
    """Provide examples for mod_or_fn if we have them & log request for examples remotely

    eg(re.sub) will print help for the re.sub module

    If an example is found we log this remotely (so we know that the example is used)
    If an example is not found we log the requrement for the example (so we know to add a new one)
    """
    if mod_or_fn is None:
        print("Supply a module or function e.g. `eg(re.sub)` to get some examples")
        return

    # strip the path names and try to get the full module (and function) name
    full_name = _get_full_name(mod_or_fn)
    # get a matching example
    match = examples.get(full_name)
    if match:
        print(match)
        log_usage(full_name, success=True)
    else:
        print("We don't know anything about '{}'...please Pull Request a new example at: https://github.com/ianozsvald/ipython_example_doc".format(full_name))
        log_usage(full_name, success=False)


if __name__ == "__main__":
    print("Example usage:")
    import pandas as pd
    eg(pd.timedelta_range)

    import re
    eg(re.sub)
