from collections import Counter, defaultdict


def most_common_technique1(data):
    """
        technique 1   -    manually populating a dict
    """
    occurs = {}
    for val in data:
        if val not in occurs.keys():
            occurs[val] = 1
        else:
            occurs[val] += 1

    most_common = sorted(occurs.items(), key=lambda pair: pair[1], reverse=True)
    return most_common[0]


def most_common_technique2(data):
    """
        technique 2   - using a default dict
    """
    occurs = defaultdict(int)
    for val in data:
        occurs[val] += 1
    most_common = sorted(occurs.items(), key=lambda pair: pair[1], reverse=True)
    return most_common[0]


def most_common_technique3(data):
    """
        technique 3   -    use of Counter
    """
    return Counter(data).most_common(1)[0]


def most_common_technique4(data):
    d = {x: data.count(x) for x in set(data)}
    return sorted(d.items(), key=lambda pair: pair[1], reverse=True)[0]