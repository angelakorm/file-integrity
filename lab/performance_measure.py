import time
from memory_profiler import memory_usage

def measure_performance(func, *args, **kwargs):
    start_time = time.time()
    mem_usage, result = memory_usage((func, args, kwargs), retval=True)
    elapsed_time = time.time() - start_time
    peak_memory = max(mem_usage) - min(mem_usage)
    return result, elapsed_time, peak_memory