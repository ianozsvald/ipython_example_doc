# ipython_example_doc
Example usages for common Python modules and functions via IPython

* Provides example usage to show how poorly-document functions can be used
* Logs a request for an example with a remote site so we can count useful-examples (which could be promoted to the original packages) and the missing examples that we need

## Usage

```
In[]: from example_doc import eg
In[]: import re  # a module we're not sure how to use
In[]: eg(re.sub)  # shows examples of usage"""
```

## Setup

Clone it from https://github.com/ianozsvald/ipython_example_doc and run setup:

```python setup.py install```

