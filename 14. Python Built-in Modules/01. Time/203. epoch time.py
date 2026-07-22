import time

epoch_time = int(time.time())
print(f"Current UNIX Epoch Time: {epoch_time}")

readable_time = time.ctime(epoch_time)
print(f"Converted Back: {readable_time}")