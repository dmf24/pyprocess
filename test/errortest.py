#!/usr/bin/env python
import sys
if __name__ == '__main__':
    try:
        arg=sys.argv[1]
    except IndexError:
        sys.exit(0)
    sys.stderr.write('Process test error output\n')
    sys.exit(int(arg))
