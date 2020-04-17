import sys
import os


def read_files(dir):
    path_files = [os.path.join(dir, name) for name in os.listdir(dir)]
    data_files = []
    for path in path_files:
        with open(path, 'r', encoding='utf8') as file:
            data = map(float, file.readlines())
        data_files.append(list(data))
    return data_files


def get_interval(queue):
    return queue[0]


def get_max_queue(queues):
    return max(enumerate(queues, start=1), key=lambda x: (x[1], -x[0]))


def main():
    DIR = sys.argv[1]
    cashs = read_files(DIR)
    sum_queue_in_intervals = list(map(sum, zip(*cashs)))
    print(get_interval(get_max_queue(sum_queue_in_intervals)))


if __name__ == '__main__':
    main()
