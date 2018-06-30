from collections import defaultdict
STATES = ["Utah", "Colorado", "Arizona", "New Mexico", "Texas"]

user_profiles = []
user_profiles.append(("Alexx", 22, "Texas", 10.5, ["egg", "fish", "bread", "steak", "chicken"]))
user_profiles.append(("Nick", 70, "Arizona", 11.5, ["cheese", "stew"]))
user_profiles.append(("Anson", 28, "Texas", 10.5, ["stew"]))
user_profiles.append(("Barb", 22, "Texas", 10.5, ["stew", "chicken", "eng", "cheese"]))

event_database = []
event_database.append((12, "Texas", ["cheese", "chicken"]))
event_database.append((17, "Arizona", ["stew"]))
event_database.append((20, "Texas", ["beef", "stew"]))


def barb(user_id, user_profiles, event_database):
    """
      user_profile[0] = name
      user_profile[1] = age
      user_profile[2] = current location
      user_profile[3] = time #limt
      user_profile[4] = [paint, food, keyword, interests]
      event_database = [(time, location,keyword)]
      """

    d = []
    curr_user = user_profiles[user_id]
    for i, event in enumerate(event_database):
        key_dict = {k: 0 for k in event[2]}
        if event[0] > curr_user[3] and event[1] == curr_user[2] and any(key in event[2] for key in curr_user[4]):
            for key in curr_user[4]:
                if key in event[2]:
                    key_dict[key] += 1
            for j, other_user in enumerate(user_profiles):
                if j != user_id and event[1] == other_user[2] and other_user[2] == curr_user[2] and event[0] > other_user[3]:
                    for key in other_user[4]:
                        if key in event[2]:
                            key_dict[key] += 1
        d.append((event, key_dict))
    d = sorted(d, key=lambda x: sum(x[1].values()), reverse=True)
    # print(d)
    if sum(d[0][1].values()) > 0:
        suggest = (d[0][0][0], d[0][0][1], [key for (key, value) in d[0][1].items() if value > 0])
    else:
        suggest = None
        for i, event in enumerate(event_database):
            if event[0] > curr_user[3] and event[1] == curr_user[2] and any(key in event[2] for key in curr_user[4]):
                suggest = (event[0], event[1], event[2])
                break

    return suggest

"""
print(barb(0, user_profiles, event_database))
print(barb(1, user_profiles, event_database))
print(barb(2, user_profiles, event_database))
print(barb(3, user_profiles, event_database))
"""