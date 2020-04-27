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
<<<<<<< HEAD
import json
from bson import json_util


odbcArray=[]

client=pymongo.MongoClient('mongodb://yechoi:0000@220.149.13.179:27017/admin')
mydb=client["bluetooth"]
scans=mydb["scans"]

print('MongoDB Connected.')
=======
from bson import json_util

client=pymongo.MongoClient("mongodb://yechoi:0000@192.168.1.32:27017/")
mydb=client["bluetooth"]
scans=mydb["scans"]

odbcArray=[]
>>>>>>> 648d9450d9bb6176b2c9be29fb3b344bc39ec774

print("Performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)



print("Found {} devices".format(len(nearby_devices)))

for addr, name in nearby_devices:
    try:
        print("   {} - {}".format(addr, name))
    except UnicodeEncodeError:
        print("   {} - {}".format(addr, name.encode("utf-8", "replace")))

<<<<<<< HEAD
#for addr,name in nearby_devices:
#    doc=collections.OrderedDict()
#    doc['address']=addr
#    doc['deviceName']=name
#    odbcArray.append(doc)

#print(odbcArray)

for addr in nearby_devices[0]:
    scans.insert_one({"address":addr})

mongoConnect.close()
=======
for addr, name in nearby_devices:
    doc=collections.OrderedDict()
    doc['address']=addr
    doc['deviceName']=name
    odbcArray.append(doc)

mongoImp=dbo.insert_many(odbcArray)
>>>>>>> 648d9450d9bb6176b2c9be29fb3b344bc39ec774
