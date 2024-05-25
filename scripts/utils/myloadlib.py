from langchain_community.document_loaders import WikipediaLoader
from langchain.document_loaders import PyPDFLoader

def loadWiki(title, lang, num_docs):
    loader = WikipediaLoader(query=title, language=lang)
    return loader.load()[:num_docs]

def loadFile(filepath):
    loader = PyPDFLoader(filepath)
    return loader.load()
