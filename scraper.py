import re
from urllib.parse import urlparse

stopWords = {"a" : 0, "about" : 0, "above" : 0, "after" : 0, "again" : 0, "against" : 0, "all" : 0, "am" : 0, "an" : 0, "and" : 0, "any" : 0, "are" : 0, "aren't" : 0, "as" : 0, "at" : 0, "be" : 0, "because" : 0, "been" : 0, "before" : 0, "being" : 0, "below" : 0, "between" : 0, "both" : 0, "but" : 0, "by" : 0, "can't" : 0, "cannot" : 0, "could" : 0, "couldn't" : 0, "did" : 0, "didn't" : 0, "do" : 0, "does" : 0, "doesn't" : 0, "doing" : 0, "don't" : 0, "down" : 0, "during" : 0, "each" : 0, "few" : 0, "for" : 0, "from" : 0, "further" : 0, "had" : 0, "hadn't" : 0, "has" : 0, "hasn't" : 0, "have" : 0, "haven't" : 0, "having" : 0, "he" : 0, "he'd" : 0, "he'll" : 0, "he's" : 0, "her" : 0, "here" : 0, "here's" : 0, "hers" : 0, "herself" : 0, "him" : 0, "himself" : 0, "his" : 0, "how" : 0, "how's" : 0, "i" : 0, "i'd" : 0, "i'll" : 0, "i'm" : 0, "i've" : 0, "if" : 0, "in" : 0, "into" : 0, "is" : 0, "isn't" : 0, "it" : 0, "it's" : 0, "its" : 0, "itself" : 0, "let's" : 0, "me" : 0, "more" : 0, "most" : 0, "mustn't" : 0, "my" : 0, "myself" : 0, "no" : 0, "nor" : 0, "not" : 0, "of" : 0, "off" : 0, "on" : 0, "once" : 0, "only" : 0, "or" : 0, "other" : 0, "ought" : 0, "our" : 0, "ours      ourselves" : 0, "out" : 0, "over" : 0, "own" : 0, "same" : 0, "shan't" : 0, "she" : 0, 
    "she'd" : 0, "she'll" : 0, "she's" : 0, "should" : 0, "shouldn't" : 0, "so" : 0, "some" : 0, "such" : 0, "than" : 0, "that" : 0, "that's" : 0, "the" : 0, "their" : 0, "theirs" : 0, "them" : 0, "themselves" : 0, "then" : 0, "there" : 0, "there's" : 0, "these" : 0, "they" : 0, "they'd" : 0, "they'll" : 0, "they're" : 0, "they've" : 0, "this" : 0, "those" : 0, "through" : 0, "to" : 0, "too" : 0, "under" : 0, "until" : 0, "up" : 0, "very" : 0, "was" : 0, "wasn't" : 0, "we" : 0, "we'd" : 0, "we'll" : 0, "we're" : 0, "we've" : 0, "were" : 0, "weren't" : 0, "what" : 0, "what's" : 0, "when" : 0, "when's" : 0, "where" : 0, "where's" : 0, "which" : 0, "while" : 0, "who" : 0, "who's" : 0, "whom" : 0, "why" : 0, "why's" : 0, "with" : 0, "won't" : 0, "would" : 0, "wouldn't" : 0, "you" : 0, "you'd" : 0, "you'll" : 0, "you're" : 0, "you've" : 0, "your" : 0, "yours" : 0, "yourself" : 0, "yourselves" : 0 }

import re
import lxml.html
import urllib
from urllib.parse import urlparse
#from bs4 import BeautifulSoup
import urllib.request
import requests

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation requred.
    links = list()
    if(resp.status >= 600 and resp.status <= 606):
        print(resp.error)
    else:
        if(resp.raw_response):
            if(resp.raw_response.status_code == 200):
                content = urllib.request.urlopen(url).read()
                html = lxml.html.document_fromstring(content)
                urls = html.xpath('//a/@href')
                for item in urls:
                    if(is_valid(item)):
                        x = requests.request('GET', item)
                        if(x.status_code == 200):
                            links.append(item)
    #if(resp.raw_response.status_code == 200):
    #    key = list(resp.raw_response.links.keys())
    #    print(resp.raw_response.links)
    #    if key:
    #        key = key[0]
    #        if key:
    #            links.append(resp.raw_response.links[key]['url'])





    return links

def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise