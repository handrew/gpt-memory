from llama_index import SimpleDirectoryReader
from gpt_memory import LocalMemoryAgent
phil = SimpleDirectoryReader("gpt_memory/examples/phil")
animals = SimpleDirectoryReader("gpt_memory/examples/animals")
phil_docs = phil.load_data()
animal_docs = animals.load_data()

memory = LocalMemoryAgent("example")
# memory.create_index("phil", phil_docs)
# memory.create_index("animals", animal_docs)
query = "Where was the protagonist Zarathustra written in?"
print(memory.query(query))
