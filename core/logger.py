import csv
import json
import os
from datetime import datetime

def save_csv(data, headers, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def append_csv(row, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def timestamped_filename(base, ext="csv"):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base}_{now}.{ext}"
