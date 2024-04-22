import argparse
import re
from bs4 import BeautifulSoup

def main(filePath): # User passes in filePath as a command line argument.
    with open(filePath, 'r', encoding="utf8") as file:
        rawData = file.read()
    
    soup = BeautifulSoup(rawData, "html.parser")

    # If the head tag exists, delete it and everything in it.
    if soup.find('head'):
        soup.find('head').decompose()

    unneededTags = ['html', 'body', 'span']

    # Remove unneeded tags, but keep the content within them.
    for tag in unneededTags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    
    # Remove empty tags and clear all tag attributes.
    for tag in soup.findAll():
        if len(tag.get_text(strip=True)) == 0:
         tag.extract()
         for val in list(tag.attrs):
            del tag.attrs[val]
    
    cleanedData = str(soup)

    # If they exist, delete all comments
    cleanedData=re.sub(r'<!.*?->','', cleanedData)

    # Remove trailing and leading spaces
    cleanedData = cleanedData.strip()
    
    with open(filePath, "w", encoding="utf8") as file:
        file.write(cleanedData)

    print("\nfile cleaned.\n")
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Allows you to pass a filename into the script."
    )

    parser.add_argument(
        '-f', '--file', metavar='file',
        required=True, help="the file you want to clean"
    )

    args = parser.parse_args()

    cleanData = main(args.file)