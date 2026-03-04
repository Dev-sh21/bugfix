import threading
import time

class buggy_gui:
    def __init__(self):
        self.iteration_counter=0

    def work(self):
        for _ in range(1000):
            # no lock here (old behaviour)
            x = self.iteration_counter
            time.sleep(0.0001)   # simulate delay / context switch
            self.iteration_counter = x+1


class fixed_gui:
    def __init__(self):
        self.iteration_counter = 0
        self.lock = threading.Lock()

    def work(self):
        for _ in range(1000):
            # with lock
            with self.lock:
                x = self.iteration_counter
                time.sleep(0.0001)
                self.iteration_counter = x + 1


def run_test(name, obj):
    print("\nRunning:", name)

    threads = []

    for i in range(50):
        t = threading.Thread(target=obj.work)
        threads.append(t)

    start = time.time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time.time()

    expected = 50 * 1000
    actual = obj.iteration_counter

    print("expected =", expected)
    print("actual   =", actual)

    if actual != expected:
        print("race condition detected, lost =", expected - actual)
    else:
        print("looks correct (no lost counts)")

    print("time =", round(end - start, 3), "sec")


if __name__ == "__main__":
    print("Thread counter test (bug vs fix)")

    buggy = buggy_gui()
    run_test("old code (no lock)", buggy)

    fixed = fixed_gui()
    run_test("fixed code (with lock)", fixed)