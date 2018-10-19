import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config-file', help='Path to config file.', required=True)
parser.add_argument('--dry-run', help='Don\'t actually update DNS records.', required=False)
args = parser.parse_args()

with open(args.config_file) as f:
    config = json.load(f)

for domain in config.keys():
    print(config[domain]['hostname'])
    print(config[domain]['password'])

