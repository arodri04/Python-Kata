def are_you_playing_banjo(name):
    print(name[0])
    if name.startswith("r") or name.startswith("R"):
        return name+" plays banjo"
    else:
        return name+" does not play banjo"
    