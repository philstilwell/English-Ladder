"""Build exact HTML identifier lookups without repeated document scans."""
from urllib.parse import unquote


def index_identifiers(soup):
    """Return first-match elements by ID plus whether an ID was duplicated."""
    identifiers = {}
    duplicate = False
    for tag in soup.select('[id]'):
        identifier = tag['id']
        if identifier in identifiers:
            duplicate = True
        else:
            identifiers[identifier] = tag
    return identifiers, duplicate


def find_identifier(identifiers, identifier, *, encoded=False):
    """Match BeautifulSoup's exact first-ID lookup, decoding URL fragments when asked."""
    if encoded:
        identifier = unquote(identifier)
    return identifiers.get(identifier)
