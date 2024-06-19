import wikipedia
from yake import yake

# build a function to learn the summary of a wikipedia page

def get_wiki_summary(page: str):
    """
    Get the summary of a wikipedia page
    """
    return wikipedia.summary(page)


# build a function search  wikipedia pages for a match

def get_wiki_pages(page: str):
    """
    Search wikipedia pages for a match
    """
    return wikipedia.page(page)


# return a keyword of a wikipedia page

def get_keywords(page: str):
    """
    Get the keywords of a wikipedia page
    """
    content = get_wiki_pages(page).content
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)
    return {keyword: score for keyword,score in keywords[:10]}







