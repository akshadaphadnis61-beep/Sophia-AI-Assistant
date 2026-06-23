import webbrowser
import pywhatkit
import wikipedia
import datetime


def openCommand(query):
    query = query.replace("open", "").strip().lower()

    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "github": "https://github.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com"
    }

    if query in sites:
        webbrowser.open(sites[query])
        return True

    return False


def PlayYoutube(query):
    query = query.replace("play", "")
    query = query.replace("on youtube", "")
    pywhatkit.playonyt(query)


def GoogleSearch(query):
    query = query.replace("search", "")
    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )


def tellTime():
    return datetime.datetime.now().strftime("%I:%M %p")


def WikiSearch(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "I could not find information."