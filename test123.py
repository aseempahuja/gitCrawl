from repo_twitter5_copy import *

import time
import random
import os
import re


def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")
arr=["co_cello", "hi", "co_hyper"]
count = 0
for x in arr:
    mat_obj=re.match("co",arr[count])
    if mat_obj:
        print arr[count]
        mat_obj=""



    count=count+1



if __name__ == "__main__":
    main()
