

user_profiles = []
user_profiles.append(("Alexx", 22, (3, 4), 10.5, [['abc.jpg', "egg", "fish"], ['cde.jpg', "bread"]]))
user_profiles.append(("Nick", 70, (5 ,6), 11.5, [['mno.jpg', "egg"], ['a.jpg', "chicken"]]))
user_profiles.append(("Anson", 28, (2, 3), 10.5, [['two.jpg', "bread", "fish", "egg"]]))
user_profiles.append(("Barb", 36, (7, 2), 10.5, [['one.jpg', "beef"]]))

def barb(user_id, user_profiles):
    """
      user_profile[0] = name
      user_profile[1] = age
      user_profile[2] = current location
      user_profile[4] = [[keyword]] keyword[0] = img path
      event_database = [(time, location,keyword)]
      """

    d = []
    curr_user = user_profiles[user_id]
    curr_keyword = set()
    curr_images = curr_user[4]
    for img in curr_images:
        for j in range(1, len(img)):
            curr_keyword.add(img[j])

    best_size = -1
    best_img = None
    best_intersect = None
    best_loc = None
    for i, other_user in enumerate(user_profiles):
        if user_id != i:
            other_images = other_user[4]
            for img in other_images:
                other_keyword = set()
                for j in range(1, len(img)):
                    other_keyword.add(img[j])
                intersect_keyword = curr_keyword.intersection(other_keyword)
                if len(intersect_keyword) > best_size:
                    best_size = len(intersect_keyword)
                    best_intersect = intersect_keyword
                    best_loc = other_user[2]
                    best_img = img[0]

    return curr_user[2], best_loc, best_img, best_intersect


print(barb(0, user_profiles))
print(barb(1, user_profiles))
print(barb(2, user_profiles))
print(barb(3, user_profiles))
