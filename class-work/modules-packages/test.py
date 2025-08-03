
from my_package import p1
from my_package.sub_package import p2

import sys

def main():
# imported from my_package
    p1.wish()
    p2.dance()
    p2.sing()


sys.exit(main())