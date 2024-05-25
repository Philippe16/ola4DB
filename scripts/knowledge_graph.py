import getpass
from langchain_experimental.graph_transformers.diffbot import DiffbotGraphTransformer
from langchain_community.graphs import Neo4jGraph
from langchain.document_loaders import WikipediaLoader

diffbot_api_token = getpass.getpass("Enter API Token: ")
diffbot_nlp = DiffbotGraphTransformer(diffbot_api_token)

# Load Wikipedia documents
raw_documents = WikipediaLoader(query="List of automobile sales by model").load()

# Convert to graph documents
graph_document_car_makes_models = diffbot_nlp.convert_to_graph_documents(raw_documents)

# Connect to Neo4j
url = "bolt://localhost:7687"
username = "neo4j"
password = "mysecretpassword"
graph = Neo4jGraph(url=url, username=username, password=password)

# Add graph documents to Neo4j
graph.add_graph_documents(graph_document_car_makes_models)
print(graph.schema)
