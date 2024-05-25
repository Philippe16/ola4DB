import os
from dotenv import load_dotenv, find_dotenv
from scripts import ingest_data, split_documents, extract_entities, organize_entities

def main():
    # Load environment variables from .env file
    load_dotenv(find_dotenv())

    # Set up data directory path
    data_dir = "data"

    # Step 1: Ingest data
    small_dataset = ingest_data.load_wiki_data("Service (motor vehicle)", "en", 3)
    medium_dataset = ingest_data.load_pdf_data(os.path.join(data_dir, "Crawfords_Auto_Repair_Guide.pdf"))
    large_dataset = ingest_data.load_pdf_data(os.path.join(data_dir, "Automotive_training.pdf"))
    large_dataset += ingest_data.load_pdf_data(os.path.join(data_dir, "how_to_change_your_car_oil.pdf"))
    large_dataset += ingest_data.load_pdf_data(os.path.join(data_dir, "honda_manual.pdf"))

    # Step 2: Split documents
    small_documents = split_documents.split_documents(small_dataset)
    medium_documents = split_documents.split_documents(medium_dataset)
    large_documents = split_documents.split_documents(large_dataset)

    # Step 3: Extract entities
    small_entities = extract_entities.extract_entities(small_documents)
    medium_entities = extract_entities.extract_entities(medium_documents)
    large_entities = extract_entities.extract_entities(large_documents)

    # Step 4: Organize entities
    organized_small_entities = organize_entities.organize_entities(small_entities)
    organized_medium_entities = organize_entities.organize_entities(medium_entities)
    organized_large_entities = organize_entities.organize_entities(large_entities)

    # Save organized entities (optional)
    # organize_entities.save_entities(organized_small_entities, "small_entities.csv")
    # organize_entities.save_entities(organized_medium_entities, "medium_entities.csv")
    # organize_entities.save_entities(organized_large_entities, "large_entities.csv")

    print("Data processing completed successfully!")

if __name__ == "__main__":
    main()
