import json

file_list = [
    "/Users/srn221b/Desktop/python-work/tweets.json",
    "/Users/srn221b/Desktop/python-work/tweets-part1.json",
]

def load_json_contents(file_path: str) -> list:
    with open(file_path, "r") as file:
        contents = file.read()
    return json.loads(contents)

if __name__ == "__main__":
    result= []
    for file_path in file_list:
        contents =load_json_contents(file_path)
        for content in contents:
            result.append(content['tweet']['full_text'])
