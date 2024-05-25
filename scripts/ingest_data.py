import myloadlib

# Load small dataset
small_dataset = []
docs = myloadlib.loadWiki("Service (motor vehicle)", "en", 3)
small_dataset.extend(docs)

# Load medium dataset
medium_dataset = []
docs = myloadlib.loadFile("data/Crawfords_Auto_Repair_Guide.pdf")
medium_dataset.extend(docs)

# Load large dataset
large_dataset = []
docs = myloadlib.loadFile("data/Automotive_training.pdf")
large_dataset.extend(docs)
docs = myloadlib.loadFile("data/how_to_change_your_car_oil.pdf")
large_dataset.extend(docs)
docs = myloadlib.loadFile("data/honda_manual.pdf")
large_dataset.extend(docs)
