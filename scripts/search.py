query = "How do I change the oil of my car?"

# Perform search
docs = small_w.similarity_search(query)
print("----- Small ------")
for i, doc in enumerate(docs):
    print(f"\nDocument {i+1}:")
    print(doc.page_content[:100] + "...")

docs = medium_w.similarity_search(query)
print("----- Medium ------")
for i, doc in enumerate(docs):
    print(f"\nDocument {i+1}:")
    print(doc.page_content[:100] + "...")

docs = large_w.similarity_search(query)
print("----- Large ------")
for i, doc in enumerate(docs):
    print(f"\nDocument {i+1}:")
    print(doc.page_content[:100] + "...")
