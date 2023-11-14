import time


def profiler(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        time.sleep(2)
        finish = time.time()
        print(f'Elapsed: {finish-start:.6f}sec')
    return wrapper


data = [1, 2, 3, 4, 5, 3, 1, 5, 2, 1, 5, 3, 4, 2, 5]


@profiler
def most_common_technique1(data):
    occurs = {}
    for val in data:
        if val not in occurs.keys():
            occurs[val] = 1
        else:
            occurs[val] += 1

    most_common = sorted(occurs.items(), key=lambda pair: pair[1], reverse=True)
    return most_common[0]


print(most_common_technique1(data))