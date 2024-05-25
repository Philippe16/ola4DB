# DB ola 4

## Overview
This project is designed to ingest, process, and search documents related to automobile maintenance. It uses various tools and libraries to load data from different sources, split them into manageable chunks, vectorize the text, store the vectors in a database, and perform similarity searches.

## Folder Structure
- `data/`: Contains PDF files used in the project.
- `scripts/`: Contains Python scripts for different stages of the project.
  - `ingest_data.py`: Loads data from Wikipedia and PDF files.
  - `split_data.py`: Splits the loaded data into smaller chunks.
  - `embed_data.py`: Vectorizes the chunks using a pre-trained model.
  - `vector_db.py`: Stores the vectors in a Weaviate vector database.
  - `search.py`: Performs similarity searches on the vector database.
  - `knowledge_graph.py`: Builds a knowledge graph from the data using Diffbot and Neo4j.
  - `utils/`: Contains utility functions used across various scripts.
    - `myloadlib.py`: Utility functions for loading data.

## Installation
1. Clone the repository.
2. Navigate to the project root directory.
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
