import weaviate
from langchain_weaviate.vectorstores import WeaviateVectorStore

# Initiate weaviate connection
weaviate_client = weaviate.connect_to_local()
assert weaviate_client.is_ready(), "Weaviate client is not ready"

# Create databases
small_w = WeaviateVectorStore.from_documents(small_documents, embedder, client=weaviate_client)
medium_w = WeaviateVectorStore.from_documents(medium_documents, embedder, client=weaviate_client)
large_w = WeaviateVectorStore.from_documents(large_documents, embedder, client=weaviate_client)
