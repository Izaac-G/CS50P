import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    regex = r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"'
    if re.search(regex, s):
        return "https://youtu.be/" + matches.group(1)
    else:
        return "None"

if __name__ == "__main__":
    main()
