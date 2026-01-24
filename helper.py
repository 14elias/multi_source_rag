from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    WebBaseLoader
)


class DocumentLoader:

    def load_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        return loader.lazy_load()

    def load_csv(self, file_path):
        loader = CSVLoader(file_path)
        return loader.lazy_load()

    def load_text(self, file_path):
        loader = TextLoader(file_path)
        return loader.lazy_load()

    def load_web(self, url):
        loader = WebBaseLoader(url)
        return loader.lazy_load()

    def load(self, source, source_type):
        if not source_type:
            raise ValueError("source_type is required")

        source_type = source_type.lower()

        match source_type:
            case "pdf":
                return self.load_pdf(source)
            case "text":
                return self.load_text(source)
            case "csv":
                return self.load_csv(source)
            case "web":
                return self.load_web(source)
            case _:
                raise ValueError(f"Unsupported source type: {source_type}")
