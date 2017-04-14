from repo_twitter5_copy import *

import time
import random
import os


def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")


    headers = {'User-Agent': '99992838f540e39d741c', 'Authorization': '3a09aed5aadfccd24b1cedf77fb22198af92a8da'}
    f = file("contributor_names.csv", 'rb')
    f_proj_name = file("proj_name.csv", 'rb')

    reader = csv.reader(f)
    proj_name_reader=csv.reader(f_proj_name)
    proj_name1=""
    for row1 in proj_name_reader:
        proj_name1= row1[0]
    count = 1
    for row in reader:
        count = count + 1
        user_name = row[0]

        print user_name, count

        isExists = os.path.exists(proj_name1)
        if not isExists:
            os.makedirs(proj_name1)
        time.sleep(10);
        listInformationForUsers(proj_name1,user_name,headers)
        # a = random.uniform(1,2)


    f.close()


if __name__ == "__main__":
    main()
