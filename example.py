from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
from gpt_memory import LocalFilesystemMemory
phil = SimpleDirectoryReader("gpt_memory/examples/phil")
animals = SimpleDirectoryReader("gpt_memory/examples/animals")
phil_docs = phil.load_data()
animal_docs = animals.load_data()

memory = LocalFilesystemMemory("example")
memory.create_index("phil", phil_docs)
animals = GPTSimpleVectorIndex.load_from_disk("animals.json")
memory.add_index("animals", animals)
query = "What is a capybara?"
