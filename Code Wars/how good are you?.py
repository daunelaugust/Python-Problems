def better_than_average(class_points, your_points):
    if (sum(class_points)/len(class_points))>your_points:
        return False
    else:
        return True# Your code here