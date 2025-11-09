from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

class ContentLoader:
    """Load and prepare text content"""
    def __init__(self, chunk_size: int=1000, chunk_overlap:int=100):
        self.splitter= RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,chunk_overlap= chunk_overlap
        )
    def load(self,file_path:str) -> List[Document]:
        """load and split content of file"""
        if file_path.endswith(".pdf"):
            loader= PyPDFLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type {file_path}")
        
        docs=loader.load()
        return self.splitter.split_documents(docs)
    
    def get_text(self, file_path: str, max_chunks:int= None) -> str:
        docs=self.load (file_path)
        if max_chunks:
            docs= docs [:max_chunks]
        return "\n\n".join([doc.page_content for doc in docs])
    