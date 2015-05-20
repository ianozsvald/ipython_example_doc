# ipython_example_doc
Example usages for common Python modules and functions via IPython

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

## Examples

* re.sub
* DataFrame's resample

## Setup

Clone it from https://github.com/ianozsvald/ipython_example_doc and run setup:

```python setup.py install```

