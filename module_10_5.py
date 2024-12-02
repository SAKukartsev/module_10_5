import datetime
from multiprocessing.pool import Pool

all_data = []


def read_info(name):
    name_ = []
    if isinstance(name, list):
        name_ = name
    else:
        name_.append(name)
    global all_data
    start_time = datetime.datetime.now()
    for file in name_:
        with open(file, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    and_time = datetime.datetime.now()
                    break
                all_data.append(line)
    time = and_time - start_time
    print(name, time)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# read_info(filenames)

# Многопроцессный
if __name__ == '__main__':
    with Pool(processes=8) as pool:
        pool.map(read_info, filenames)
