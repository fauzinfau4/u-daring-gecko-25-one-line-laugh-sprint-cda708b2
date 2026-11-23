import os

LINE = "The robot vacuum mapped my apartment, then parked by the laundry pile; even AI knows where danger lives."

os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as entry:
    entry.write(LINE + '\n')
