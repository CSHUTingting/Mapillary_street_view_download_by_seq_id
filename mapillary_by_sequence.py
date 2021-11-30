import mercantile, mapbox_vector_tile, requests, json
from vt2geojson.tools import vt_bytes_to_geojson
from haversine import haversine

import os
import json
import urllib.request
import sys
import time
import pandas as pd

save_path = 'D:\python'  #saving path

def Get_streetview_by_seq (seq_id):
    if not os.path.exists(save_path + '/' + seq_id):  # create filefolder of images
        os.makedirs(save_path + '/' + seq_id)

    access_token = 'MLY|4849862328377223|906ddbe641b30cffed6835ccce925d65'
    header = {'Authorization': 'OAuth {}'.format(access_token)}
#    url = 'https://graph.mapillary.com/{}?fields=thumb_2048_url'.format(image_id)   #using image id request image url
    url = "https://graph.mapillary.com/image_ids?sequence_id={}".format(seq_id)
    print(url)
    r = requests.get(url, headers=header)
    data = r.json()
    print(data)

    print(data["data"][1]["id"])


    for i in range(len(data["data"])):
        image_id = data["data"][i]["id"]
        url = 'https://graph.mapillary.com/{}?fields=thumb_2048_url,geometry'.format(image_id)
        r = requests.get(url, headers=header)
        data1 = r.json()
        print(data1['thumb_2048_url'])
        print(str(data1['geometry']['coordinates'][1]))

        image_url = data1['thumb_2048_url']
        coords = data1['geometry']['coordinates']
        req = urllib.request.Request(url=image_url, headers=header)  # request download image
        response = urllib.request.urlopen(req)
        raw_img = response.read()
        print("request successful")

        file_out = save_path  + '/' + seq_id + '/' + str(coords[0]) + ',' + str(coords[1]) + ".jpg"  # save image
        if not os.path.exists(file_out):  # create filefolder of images
            f = open(file_out, "wb")
            f.write(raw_img)
            f.close




Get_streetview_by_seq (seq_id="P69cCTldQwekNtfO1gRxAy") #sequence id

