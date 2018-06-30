import boto3
import os
BUCKET = "amazon-rekognition-cin"
KEY = "1.jpg"

def detect_labels(bucket, key, max_labels=10, min_confidence=.6, region="us-east-1"):
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
def syn():
    syn_image = 'aws s3 sync image s3://{}'.format(BUCKET)
    os.system(syn_image)

from pyson_utils import image
paths = image.get_paths("image", "jpg")

def path2objects(path):
    KEY = path#path.split('/')[-1]
    rv = detect_labels(BUCKET, KEY)
    # for label in rv:
    #     print ("{Name} - {Confidence}%".format(**label))
    return rv
# aws rekognition detect-labels --image "S3Object={Bucket="clicksmile",Name="/Users/Bi/Downloads/20180614_180755.jpg"}"
syn()
json_1 = path2objects('1/1.jpg')
json_2 = path2objects('2/2.jpg')
print(json_1, json_2)