from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    WebBaseLoader
)


class DocumentLoader:

    def _load_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        return loader.lazy_load()

    def _load_csv(self, file_path):
        loader = CSVLoader(file_path)
        return loader.lazy_load()

    def _load_text(self, file_path):
        loader = TextLoader(file_path)
        return loader.lazy_load()

    def _load_web(self, url):
        loader = WebBaseLoader(url)
        return loader.lazy_load()

    def load(self, source, source_type):
        print(source_type)
        if not source_type:
            raise ValueError("source_type is required")

        source_type = source_type.lower()

        match source_type:
            case s if s.startswith('application/pdf'):
                return self._load_pdf(source)
            case s if s.startswith('text'):
                return self._load_text(source)
            case s if s.startswith('csv'):
                return self._load_csv(source)
            case s if s.startswith('web'):
                return self._load_web(source)
            case _:
                raise ValueError(f"Unsupported source type: {source_type}")


document_loader = DocumentLoader()