# -*- coding:utf-8 -*-

from pymongo import (
    # MongoReplicaSetClient,
    MongoClient,
    # read_preferences
)
import gridfs

# import setting

mc = MongoClient(host='localhost')

# test
test = mc['test']
test_files = gridfs.GridFS(mc['test_files'])

# certificate
dc = mc['hayate']
dc_files = gridfs.GridFS(mc['hayate_files'])
