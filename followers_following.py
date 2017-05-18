from repo_twitter_copy import *
from repo_twitter2_copy import *
from repo_twitter3_copy import *
from repo_twitter4_copy import *
from repo_twitter5_copy import *
import re

import time
import random
import os


def listInformationForUsers(proj_name1,user_name, headers):
    followers = listFollowers(user_name, headers)
    writeFollowersToCSV(proj_name1, user_name,followers)
    following = listFollowing(user_name, headers)
    writeFollowingToCSV(proj_name1, user_name, following)

def listFollowers(user_name, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(10)
       #file_name = "http://api.github.com/repos/" + user_name + "/%s/contributors?per_page=100&page=%d" % (repos, j)
        #/users/jyellick/followers
        file_name = "http://api.github.com/users/%s/followers?per_page=100&page=%d" % (user_name, j)
        repo_followers = requests.get(file_name, headers)
        # print repo_contributors, j#if success(200)
        raw_data = json.loads(repo_followers.text)
        #print raw_data
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    ##print len(data)##print the number of repository
    return data

def writeFollowersToCSV(proj_name1, repo, contributors):  # write to csv

    f = csv.writer(open(proj_name1 + "/" + time.strftime("%d%m%Y") + repo + "_Followers.csv", "wb+"))
    # write_header = True
    item_keys = []
    item_values = []

    for i in range(len(contributors)):
        singleContributor = contributors[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for j in range(len(singleContributor.keys())):

            if write_header:
                item_keys.append(singleContributor.keys()[j])
            value = singleContributor.get(singleContributor.keys()[j])
            item_values.append(value)

        if write_header:
            ##print item_values
            f.writerow(item_keys)
        ##print item_values
        f.writerow(item_values)

def listFollowing(user_name, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(1)

        file_name = "http://api.github.com/users/%s/following?per_page=100&page=%d" % (user_name, j)
        repo_followers = requests.get(file_name, headers)
        print repo_followers.headers
        # print repo_contributors, j#if success(200)
        raw_data = json.loads(repo_followers.text)
        #print raw_data
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    ##print len(data)##print the number of repository
    return data

def writeFollowingToCSV(proj_name1, repo, contributors):  # write to csv

    f = csv.writer(open(proj_name1 + "/" + time.strftime("%d%m%Y") + repo + "_Following.csv", "wb+"))
    # write_header = True
    item_keys = []
    item_values = []

    for i in range(len(contributors)):
        singleContributor = contributors[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for j in range(len(singleContributor.keys())):

            if write_header:
                item_keys.append(singleContributor.keys()[j])
            value = singleContributor.get(singleContributor.keys()[j])
            item_values.append(value)

        if write_header:
            ##print item_values
            f.writerow(item_keys)
        ##print item_values
        f.writerow(item_values)


def main():
    #post all contributors logins into one file preceded by the contributors_of_<proj_name>
    #the program will sense it is a new project and make a new directory where everything will be stored
    reload(sys)
    sys.setdefaultencoding("utf-8")

    matching_argz="contributors_of"
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
        user_name = row[0]

        print user_name, count
        count = count + 1

        matchObj=re.match(matching_argz, user_name)
        if matchObj:
            #time to change the directory
            isExists = os.path.exists(user_name)
            if not isExists:
                os.makedirs(user_name)
            proj_name1=user_name
            time.sleep(3600)
        else:
            #else store the info
            time.sleep(10);
            listInformationForUsers(proj_name1,user_name,headers)
            # a = random.uniform(1,2)


    f.close()


if __name__ == "__main__":
    main()
