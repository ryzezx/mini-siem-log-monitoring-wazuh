#!/usr/bin/env python3
import json, time, argparse, csv, os
from pathlib import Path

def parse_alert(line):
    try:
        data = json.loads(line)
        return {
            'timestamp': data.get('timestamp', ''),
            'rule.level': data.get('rule', {}).get('level', ''),
            'srcip': data.get('srcip', ''),
            'description': data.get('description', data.get('full_log', ''))
        }
    except Exception:
        return None

parser = argparse.ArgumentParser()
parser.add_argument('--live', action='store_true')
parser.add_argument('--csv', type=str, default='')
args = parser.parse_args()

log_path = '/var/ossec/logs/alerts/alerts.json'
if args.live:
    with open(log_path, 'r') as f:
        f.seek(0, 2)
        with open(args.csv, 'w', newline='') if args.csv else open(os.devnull, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['timestamp','rule.level','srcip','description'])
            if args.csv: writer.writeheader()
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                alert = parse_alert(line)
                if alert:
                    print(alert)
                    if args.csv: writer.writerow(alert)
