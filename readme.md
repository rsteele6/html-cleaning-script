# HTML Cleaning Script

## Description

This is a short script written in Python that performs the following on HTML files:

- Removes:
  - `<head>` and all its content
  - `<span>` (keeps content)
  - `<html>`
  - `<body>`
  - empty tags
  - all tag attributes (classes, etc.)
  - comments
  - trailing and leading spaces

I used the Beautiful Soup module to perform most of the operations. The script can be used to prepare raw HTML files for import into content management systems.

## Arguments

-f \<filepath\> or --file \<filepath\>, where \<filepath\> is the relative path to the file you want to clean. For example:

```
python clean-html.py -f example.html
```

or

```
python clean-html.py --file example.html
```

## Libraries

- Beautiful Soup
- re
- argparse
