from langchain.text_splitter import TokenTextSplitter

# Define chunking strategy
smallSplitter = TokenTextSplitter(chunk_size=100, chunk_overlap=10)
mediumSplitter = TokenTextSplitter(chunk_size=500, chunk_overlap=100)
largeSplitter = TokenTextSplitter(chunk_size=256, chunk_overlap=52)

# Split documents
small_documents = smallSplitter.split_documents(small_dataset)
medium_documents = mediumSplitter.split_documents(medium_dataset)
large_documents = largeSplitter.split_documents(large_dataset)

print(len(small_documents))
print(len(medium_documents))
print(len(large_documents))
