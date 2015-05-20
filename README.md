# Example usages for common Python modules and functions via IPython

Why? I spend a lot of time looking up the same infrequently-used function through StackOverflow, the cause is poor documentation at the command line. This tool aims to identify which examples are needed so we can improve the original function's documentation.

Aims:
* Provides example usage to show how poorly-document functions can be used
* Logs a request for an example with a remote site so we can count useful-examples (which could be promoted to the original packages) and the missing examples that we need

## Usage

```
In [1]: from example_doc.eg import eg
In [2]: import re  # a module we're not sure how to use
In [3]: eg(re.sub)
sub allows direct substitutions from a pattern match:
re.sub('\d+', "WASANUMBER", "stuff and 23, 55, no more")
'stuff and WASANUMBER, WASANUMBER, no more'

It also allows for more complex functions (e.g. a lambda) to be called:
re.sub('\d+', lambda match_obj: str(int(match_obj.group(0))*2), "stuff and 23, 55, no more")
'stuff and 46, 110, no more'

In [4]: import pandas as pd
In [5]: df=pd.DataFrame()
In [6]: eg(df.resample)
resample(rule="1D", how="sum")
rule can have the form '5Min' (minute), '2h' (hour), 'D' (day), '2D' (2 day), 'M' (month)
Common rules: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
how can use 'sum', 'mean', 'ohlc', np.max, np.mean

In [7]: eg(df.asfreq)  # How to document something we don't know about
We don't know anything about 'pandas.core.generic.asfreq'...please Pull Request a new example at: https://github.com/ianozsvald/ipython_example_doc



```

## Examples we have (we need more!)

* `re.sub`
* DataFrame's `resample`

To add an example - either file a bug against this project or (better) make a Pull Request which updates the `examples` dictionary.

Requested examples:

* `urllib.request.urlopen` has a `timeout` which is not documented (it can be a float...), see my usage in `log_usage`
* `pandas.tseries.tdi.timedelta_range`
* any Pandas method with a `how` or `method` where the user is left to guess at the various `how` options
* datetime conversions (notably: how to parse dates (even if using other tools like date-util), how to convert dates)
* matplotlib common calls (e.g. use of alpha, custom xticks, rotated text) where an example would save hunting through the existing documentation
* Other stuff you keep repeatedly search for in Google and StackOverflow

## Setup

Clone it from https://github.com/ianozsvald/ipython_example_doc and run setup:

```python setup.py install```

## TODO ?

  * rather than synchronously log the result (log_result), use a thread for async logging
