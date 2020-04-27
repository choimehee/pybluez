#!/usr/bin/env python3
"""PyBluez simple example inquiry.py

Performs a simple device inquiry followed by a remote name request of each
discovered device

Author: Albert Huang <albert@csail.mit.edu>
$Id: inquiry.py 401 2006-05-05 19:07:48Z albert $
"""

import bluetooth
import pymongo
import collections
from bson import json_util


client=pymongo.MongoClient('mongodb://yechoi:0000@220.149.13.179:27017/admin')
mydb=client["bluetooth"]
scans=mydb["scans"]

print('MongoDB Connected.')

odbcArray=[]

print("Performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)



print("Found {} devices".format(len(nearby_devices)))

for addr, name in nearby_devices:
    try:
        print("   {} - {}".format(addr, name))
    except UnicodeEncodeError:
        print("   {} - {}".format(addr, name.encode("utf-8", "replace")))


for addr in nearby_devices[0]:
    scans.insert_one({"address":addr})

#for addr, name in nearby_devices:
#    doc=collections.OrderedDict()
#    doc['address']=addr
#    doc['deviceName']=name
#    odbcArray.append(doc)
