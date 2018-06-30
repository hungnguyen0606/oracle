import sys
import os
import matplotlib as mpl
from time import sleep
from barb import barb
from PIL import Image
from rekog_person import get_keywords
import matplotlib.pyplot as plt

DEBUG = True

def syn():
   syn_image = 'aws s3 sync s3://amazon-rekognition-cin image'
   os.system(syn_image)

def make_profiles():
    profiles = []
    for person in os.listdir('image'):
        keywords = get_keywords(person)
        if DEBUG:
            print(f'done for {person}') 
        profile = (person, 22, (, 4), 10.5, [['abc.jpg', "egg", "fish"], ['cde.jpg', "bread"]])
        profiles.append(profile)

if __name__ == '__main__':
    title = '''


        ,----,                                                                                            
      ,/   .`|                                 ,----..                                                    
    ,`   .'  :  ,---,                         /   /   \                                 ,--,              
  ;    ;     /,--.' |                        /   .     :                              ,--.'|              
.'___,/    ,' |  |  :                       .   /   ;.  \  __  ,-.                    |  | :              
|    :     |  :  :  :                      .   ;   /  ` ;,' ,'/ /|                    :  : '              
;    |.';  ;  :  |  |,--.   ,---.          ;   |  ; \ ; |'  | |' | ,--.--.     ,---.  |  ' |      ,---.   
`----'  |  |  |  :  '   |  /     \         |   :  | ; | '|  |   ,'/       \   /     \ '  | |     /     \  
    '   :  ;  |  |   /' : /    /  |        .   |  ' ' ' :'  :  / .--.  .-. | /    / ' |  | :    /    /  | 
    |   |  '  '  :  | | |.    ' / |        '   ;  \; /  ||  | '   \__\/: . ..    ' /  '  : |__ .    ' / | 
    '   :  |  |  |  ' | :'   ;   /|         \   \  ',  / ;  : |   ," .--.; |'   ; :__ |  | '.'|'   ;   /| 
    ;   |.'   |  :  :_:,''   |  / |          ;   :    /  |  , ;  /  /  ,.  |'   | '.'|;  :    ;'   |  / | 
    '---'     |  | ,'    |   :    |           \   \ .'    ---'  ;  :   .'   \   :    :|  ,   / |   :    | 
              `--''       \   \  /             `---`            |  ,     .-./\   \  /  ---`-'   \   \  /  
                           `----'                                `--`---'     `----'             `----'   
                                                                                                          

'''
    print(title)
    sleep(0.4)
    text = 'Based on your latest images\nthe Oracle got a divine message for you'
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)
    for _ in range(3):
        sleep(.4)
        sys.stdout.write('.')
        sys.stdout.flush()
    the_place = 'Nowhere™'
    the_time = 'Midnight'
    text = f'\nGo to {the_place} at {the_time} for a striking encounter that has somthing to do with this img'
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)
    sleep(0.4)
    img = Image.open('data/jack.png')
    plt.imshow(img)
    plt.show()
    input('\nGo, go now! And come back to me when you\'re there')
    text = 'Now you\'re wondering what the secret to the prophecy is. Your image matched with images from user {},'\
            'both of you are interested in {}, here\'s your version and here\'s user {} version.' 
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)
    text = 'A match made in heaven, I\'d say!'
