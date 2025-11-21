# Report generator
import json

def generate_report(results, output_file='report/report.json'):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

