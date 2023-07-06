from pathlib import Path
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenLLM

loader = DirectoryLoader(
    str(Path.home() / "courses/DO378/content"),
    glob="**/*.adoc",
    recursive=True,
    show_progress=True,
    use_multithreading=True)

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1000,
    chunk_overlap  = 2,
    length_function = len,
    add_start_index = True,
)

# llm = OpenLLM(server_url="http://localhost:3000")
llm = OpenLLM(
    model_name="opt",
    model_id="facebook/opt-125m",
    temperature=0.94,
    repetition_penalty=1.2,
)

docs = text_splitter.split_documents(loader.load())
chain = load_qa_chain(llm, chain_type="map_reduce")
result = chain.run(
    input_documents=docs,
    question="Name one easy way to deploy an Application in OpenShift"
)

print(result)

