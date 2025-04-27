import argparse
import sys
import json
from jsonpath_ng.ext import parse as jsonpath_parse

def main():
    parser = argparse.ArgumentParser(description="Simple JSONPath query tool")
    parser.add_argument('jsonpath', help='JSONPath expression')
    parser.add_argument('--file', '-f', type=argparse.FileType('r'), default=sys.stdin, help='Input JSON file (default: stdin)')
    args = parser.parse_args()

    data = json.load(args.file)
    expr = jsonpath_parse(args.jsonpath)
    matches = expr.find(data)
    results = [match.value for match in matches]

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()

