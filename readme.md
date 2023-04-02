# 🧠 GPT Memory

LocalFilesystemMemory is a layer over Llama Index's GPTSimpleVectorIndex which
abstracts away the details of managing indexes saved on disk. It assumes /
creates a directory structure for storing indexes and provides a simple /
interface for managing them.

## LocalFilesystemMemory

1. Instantiate the memory with a folder where it will store its persistent memory.
2. Create and name indexes. It will automatically generate a summary of the documents you provide.
3. When you are ready, you can query the memory, and it will proceed in two steps. (a) It will figure out which of the named indexes is the right one to load into memory and query, based on how your query matches against the previously generated summaries. (b) It will then run that query against the most relevant index.

An example using some Wikipedia files you can find in this repo:

```python
from llama_index import SimpleDirectoryReader
from gpt_memory import LocalFilesystemMemory
phil = SimpleDirectoryReader("gpt_memory/examples/phil")
animals = SimpleDirectoryReader("gpt_memory/examples/animals")
phil_docs = phil.load_data()
animal_docs = animals.load_data()

memory = LocalFilesystemMemory("example")
memory.create_index("phil", phil_docs)
memory.create_index("animals", animal_docs)
query = "What is a capybara?"
print(memory.query(query))
```

Returns: ```A capybara is a giant cavy rodent native to South America, which is the largest living rodent and a member of the genus Hydrochoerus. It inhabits savannas and dense forests, lives near bodies of water, and is a highly social species that can be found in groups as large as 100 individuals. The capybara is hunted for its meat and hide and also for grease from its thick fatty skin, but it is not considered a threatened species.```

### Methods

- ```memory.query(prompt)```: The main entrypoint to ask a question.
- ```memory.create_index(name, docs, description=None)```: The main way to create an index. Docs can be strings, lists of strings, or lists of GPTIndex's Document objects.
- ```memory.update_index(name, docs)```: Update an index with new docs.
- ```memory.delete_index(name)```: Delete an index.

Under the hood, those functions use:
- ```memory.get_index(name)```
- ```memory.query_index(name, prompt)```
- ```memory.find_most_relevant_index(prompt)```


### Under the hood
Under the hood, the directory structure is as follows:
```
- index_folder/
    -  metadata.json
    -  indexes/
        -  index_1.json
        -  index_2.json
        -  ...
```

The metadata.json file contains the following information:

```
{
    "index_count": 2,
    "index_descriptions": [
        {
            "name": "index_1",
            "description": "Description of index generated by GPT Index.",
        },
        {
            "name": "index_2",
            "description": "Description of index generated by GPT Index.",
        },
    ]
}
```


