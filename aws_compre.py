import pandas 
import boto3
import json
import urllib3
import re
from tqdm import tqdm
import html2text
import os
def extract_entity(text):
    text = text[:4555]
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    # text = "It is raining today in Seattle"

    return json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)

def extract_keyword(text):
    text = text[:4555]
    comprehend = boto3.client(service_name='keyword', region_name='us-east-1')
    # text = "It is raining today in Seattle"

    return json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)



def get_text(target_url):
    http = urllib3.PoolManager()       
    response = http.request('GET', target_url)
    data = response.data.decode('utf-8')
    data = html2text.html2text(data)
    data = data.replace('\n', '')
    return data
# print(extract_entity("Hello my name is Anson"))

def export(name, json):
    with open(name, 'w') as f:
        f.write(json)


def read_reviews(csv_path):
    df = pandas.read_csv(csv_path)
    texts = [_ for _ in df["Text"]]
    rv = []
    for text in tqdm(texts[:10]):
        extracted_keys = extract_entity(text)
        rv.append(extracted_keys)
    return rv


# rv = read_reviews("wikipedia_utf8_filtered_20pageviews.csv")
f = open("wikipedia_utf8_filtered_20pageviews.csv", "r")
line = f.readline()
j = extract_entity(line)
print(j)