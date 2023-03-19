# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    for i in range(m):
        min_time = threads[0]
        min_thread = 0
        for j in range(1, n):
            if threads[j] < min_time:
                min_time = threads[j]
                min_thread = j
        output.append((min_thread, min_time))
        threads[min_thread] += data[i]
    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()
