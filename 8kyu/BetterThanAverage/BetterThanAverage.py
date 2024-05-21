def better_than_average(class_points, your_points):
    
    count = 0
    for i in class_points:
        count += i
    count = count / len(class_points)
    if count < your_points:
        return True
    else:
        return False