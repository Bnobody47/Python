import webbrowser as wb
def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' #Add the path of chrome here
    URLS = (
        "https://www.google.com/",
        "https://www.youtube.com/",
        "https://www.stackoverflow.com"
    )
    for url in URLS:
        wb.get(chrome_path).open(url)

webauto()
