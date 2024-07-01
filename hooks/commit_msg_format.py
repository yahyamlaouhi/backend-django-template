import sys
import re

def check_commit_msg_format(commit_msg_file):
    with open(commit_msg_file) as f:
        commit_msg = f.read().strip()

    pattern = r'^(\w+) : (.+)$'
    if not re.match(pattern, commit_msg):
        print(f"Invalid commit message format: {commit_msg}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(check_commit_msg_format(sys.argv[1]))
