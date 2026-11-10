import threading


counter = 0
lock = threading.Lock()


def worker() -> None:
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1


def main() -> None:
    threads = [threading.Thread(target=worker) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(counter)


if __name__ == "__main__":
    main()
