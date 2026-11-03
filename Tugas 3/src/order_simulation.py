
import threading
import random
import time

NUM_ORDERS = 100
NUM_WORKERS = 10

processed_count = 0
lock = threading.Lock()

# Percobaan pertama: tanpa Lock


def process_order(order_id: int) -> None:
    global processed_count

    time.sleep(random.uniform(0.001, 0.01))

    # Simulasi race condition
    with lock:
        processed_count += 1


def worker(order_ids: list) -> None:
    for order_id in order_ids:
        process_order(order_id)


def main() -> None:
    order_ids = list(range(1, NUM_ORDERS + 1))

    threads = []

    for i in range(NUM_WORKERS):
        order_chunk = order_ids[i::NUM_WORKERS]
        t = threading.Thread(target=worker, args=(order_chunk,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"Total pesanan diproses: {processed_count} (seharusnya {NUM_ORDERS})")

    if processed_count != NUM_ORDERS:
        print("RACE CONDITION TERDETEKSI!")
    else:
        print("Counter sesuai target.")


if __name__ == "__main__":
    main()
