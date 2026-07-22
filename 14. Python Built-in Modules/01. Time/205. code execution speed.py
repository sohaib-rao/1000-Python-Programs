import time

start_time = time.perf_counter()

total = sum(range(1000000)) 

end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000  

print(f"Task completed. Execution Time: {execution_time:.2f} ms")