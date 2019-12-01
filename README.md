# pyprocess
Python subprocess wrappers

This module is probably obsolete for anyone able to use [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run) for all their needs.  I originally began using these wrappers before `subprocess.run` was available and found that these scripts cover the overwhelming majority of my subprocess needs, and personally find them noticeably more convenient than even subprocess.run.  Specifically, almost always I want to:

1.  Format my whole command as a string which is passed to `shlex.split`.
2.  Call subprocess.Popen with PIPE for stdout and stderr, and sometimes with stdin set.
3.  Get the return code, stdout, and stderr as an unnamed tuple, with out and err decoded to utf-8.  I don't need it named.  0 for return code, 1 for standard out, and 2 for standard error are standard and trivial to memorize.

That's it.  Sometimes I want to run multiple simultaneously and don't want to block on a single process.  Every so often I want to use a python string and send it to a process's stdin.

And I (still, even in 2019) need it to be compatible with multiple versions of python, not just Python 3.

Hence, this library.

```Python
>>> from process import process
>>> process('echo 1 2')
(0, '1 2\n', '')
>>> process('test/errortest.py 5')
(5, '', 'Process test error output\n')
```
