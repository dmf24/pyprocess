# pyprocess
Python subprocess wrappers

This module is probably obsolete for anyone able to use [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run) for all their needs.  I originally began using these wrappers before `subprocess.run` was available and found that these scripts cover the overwhelming majority of my subprocess needs.

```Python
>>> from process import process
>>> process('echo 1 2')
(0, '1 2\n', '')
>>> process('test/errortest.py 5')
(5, '', 'Process test error output\n')
```

