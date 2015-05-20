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
```

## Examples we have (we need more!)

* re.sub
* DataFrame's resample

To add an example - either file a bug against this project or (better) make a Pull Request which updates the `examples` dictionary.

Requested examples:

* any Pandas method with a `how` or `method` where the user is left to guess at the various `how` options
* datetime conversions (notably: how to parse dates (even if using other tools like date-util), how to convert dates)
* matplotlib common calls (e.g. use of alpha, custom xticks, rotated text) where an example would save hunting through the existing documentation
* Other stuff you keep repeatedly search for in Google and StackOverflow

## Setup

Clone it from https://github.com/ianozsvald/ipython_example_doc and run setup:

```python setup.py install```

