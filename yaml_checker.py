import sys
import yaml

args = sys.argv
with open(args[1], 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
print(data)