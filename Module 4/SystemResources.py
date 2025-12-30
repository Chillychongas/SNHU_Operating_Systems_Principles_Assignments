"""
Author: Andrew Ferasol
Due Date: 12/07/2025
Description:
fetches hig-level CPU and memory information sucha s:
Total CPU usage and CPU count
Total memory available and memory usage
"""

import psutil

#cpu stats
print(f"CPU Usage:\t {psutil.cpu_percent(interval = 0.1)}%")
print(f"CPU Count:\t {psutil.cpu_count()}")

#memory stats
memory = psutil.virtual_memory()
print(f"Mem Available:\t {memory.available}")
print(f"Mem Usage:\t {memory.percent}%")