from time import sleep, perf_counter


def count():
    sleep(1)
    print(1)
    sleep(2)
    print(2)
    sleep(3)
    print(3)


def main():
    t1 = perf_counter()
    count()
    count()
    count()
    t2 = perf_counter()
    print(f"Took {(t2 - t1):.2f} seconds")


if __name__ == "__main__":
    main()
