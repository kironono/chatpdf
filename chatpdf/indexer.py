from llama_index import download_loader
from llama_index import GPTSimpleVectorIndex


class Indexer:

    def __init__(self, config, source):
        self.config = config
        self.source = source

    def execute(self):
        CJKPDFReader = download_loader("CJKPDFReader")
        loader = CJKPDFReader()

        documents = []
        for pdf in self.source.glob("**/*.pdf"):
            d = loader.load_data(file=pdf)
            documents.extend(d)

        index = GPTSimpleVectorIndex.from_documents(
                documents, service_context=self.config.service_context)
        index.save_to_disk(self.config.index_file)
