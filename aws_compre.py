import boto3
import json
def extract_entity(text):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    # text = "It is raining today in Seattle"

    return json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)


print(extract_entity("Hello my name is Anson"))