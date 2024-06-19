import wikipedia

# build a function to learn the summary of a wikipedia page

def get_wiki_summary(page: str):
    """
    Get the summary of a wikipedia page
    """
    return wikipedia.summary(page)


# build a function search  wikipedia pages for a match

def search_wiki_pages(page: str):
    """
    Search wikipedia pages for a match
    """
    return wikipedia.search(page)




