

def threshold(lst, th):
    new = []
    if len(lst) > th:
        return "The length of the list is more than the threshold number"
    else:
        for i, val in enumerate(lst):
            new.append(i)
        return new


threshold([0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55],100)











