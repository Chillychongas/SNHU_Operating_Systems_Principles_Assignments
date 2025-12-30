"""
Author: Andrew Ferasol
Due Date: 11/23/2025
Description:
fetches all processes currently running on the system and displays the:
id, name, memory percentm, and cpu percent (through a .1 sec interval)
"""
import psutil

for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
    try:
        pid = proc.info['pid']
        name = proc.info['name'] or 'N/A'
        mem = proc.info['memory_percent']
        cpu = proc.cpu_percent(interval = 0.1)
        
        print(f"{pid:<6}{name[:29]:<30}{mem:<12.2f}{cpu:<10.2f}")
        
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue