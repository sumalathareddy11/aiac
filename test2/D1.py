import re
import os

def bump_version(name):
    base, ext = os.path.splitext(name)
    # Look for _vNN at the end of the base name
    match = re.search(r'(.*)_v(\d+)$', base)
    if match:
        prefix = match.group(1)
        num = match.group(2)
        new_num = str(int(num) + 1).zfill(len(num))
        new_base = f"{prefix}_v{new_num}"
    else:
        new_base = f"{base}_v01"
    return new_base + ext

if __name__ == "__main__":
    files = input("Enter file names separated by commas: ").split(",")
    files = [f.strip() for f in files if f.strip()]
    bumped = [bump_version(f) for f in files]
    print("Bumped versions:")
    for f in bumped:
        print(f)
