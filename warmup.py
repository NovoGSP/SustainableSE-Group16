import multiprocessing
import time

def fibonacci(n):
    """Compute the nth Fibonacci number iteratively."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def warm_up_worker(duration, fib_steps):
    """
    Worker function that repeatedly computes Fibonacci numbers
    for a specified duration.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        fibonacci(fib_steps)

if __name__ == '__main__':
    # Duration of the warm-up (in seconds). 5 minutes = 300 seconds.
    DURATION = 5 * 60  
    # Number of iterations for the Fibonacci function.
    FIB_STEPS = 1000  
    # Use the number of available CPU cores.
    NUM_PROCESSES = multiprocessing.cpu_count()

    print(f"Starting CPU warm-up on {NUM_PROCESSES} processes for {DURATION} seconds...")

    processes = []
    for _ in range(NUM_PROCESSES):
        p = multiprocessing.Process(target=warm_up_worker, args=(DURATION, FIB_STEPS))
        p.start()
        processes.append(p)

    # Wait for all processes to complete.
    for p in processes:
        p.join()

    print("CPU warm-up complete!")
