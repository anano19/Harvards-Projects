
import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search('src=\"(.*?)\"', s)
    if match:
        url = match.group(1)
    video_match = re.search('/embed/(.*)', url)
    if video_match:
        video = video_match.group(1)
        short = "https://youtu.be/" + video
        return short
    else:
        return None




if __name__ == "__main__":
    main()
