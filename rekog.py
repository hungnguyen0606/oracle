import boto3
from glob import glob
import os

BUCKET = "amazon-rekognition-cin"
KEY = "1.jpg"

exts = ['png', 'jpg', 'jpeg']

def detect_labels(bucket, key, max_labels=10, min_confidence=0, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    return response['Labels']


def get_keywords(person):
    ret = []
    ll = []
    for ext in exts:
        path = os.path.join('./image', person, '*.%s'%ext)
        limgs = glob(path)
        ll.extend(limgs)

    tmp = []
    for im in ll:
        im = os.path.basename(im)
        tmp.extend(detect_labels(BUCKET, os.path.join(person, im)))

    ret = [e['Name'] for e in tmp if e['Name'] not in ['Human', 'People', 'Person']]    

    return ret

def syn():
    syn_image = 'aws s3 sync image s3:/{}'.format(BUCKET)
    os.system(syn_image)

# from pyson_utils import image
# paths = image.get_paths("image", "jpg")

def path2objects(path):
    KEY = path.split('/')[-1]
    rv = detect_labels(BUCKET, KEY)
    # for label in rv:
    #     print ("{Name} - {Confidence}%".format(**label))
    return rv
# aws rekognition detect-labels --image "S3Object={Bucket="clicksmile",Name="/Users/Bi/Downloads/20180614_180755.jpg"}"

print(get_keywords('taylor'))