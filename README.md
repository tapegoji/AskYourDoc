# AskYourDoc

A powerful document query tool that leverages LangChain and various language models to extract information from technical PDF documents.

## Overview

AskYourDoc allows you to load PDF documents (especially technical datasheets), store them in a vector database, and query them using natural language. The tool uses RAG (Retrieval-Augmented Generation) to efficiently process large documents and provides accurate answers to your questions.

## Features

- Load and process PDF documents using DoclingLoader
- Store document embeddings in a persistent ChromaDB database
- Support for various language models (Groq, OpenAI, Anthropic, Ollama)
- RAG implementation for efficient document querying
- Structured response formatting using Pydantic

## Prerequisites

- Python 3.8+
- Jupyter Notebook environment
- API keys for the language model providers you plan to use

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AskYourDoc.git
   cd AskYourDoc
   ```

2. Install required dependencies:
   ```bash
   pip install langchain langchain-openai langchain-docling chromadb pydantic
   ```

## Environment Setup

You need to set up your API keys as environment variables before running the code. The following API keys are used in the project:

- `GROQ_API_KEY` - For using Groq models
- `OPENAI_API_KEY` - For using OpenAI models and embeddings
- `ANTHROPIC_API_KEY` - For using Anthropic Claude models

You can set these environment variables before running your notebook:

```bash
export GROQ_API_KEY="your-api-key"
export OPENAI_API_KEY="your-api-key"
export ANTHROPIC_API_KEY="your-api-key"
```

Alternatively, the code will prompt you to enter your API keys if they're not found in environment variables.

## Usage

1. Place your PDF documents in the `docs/` folder.

2. Open and run the `main.ipynb` notebook:
   ```bash
   jupyter notebook main.ipynb
   ```

3. The notebook contains cells to:
   - Load documents from PDFs
   - Create and manage a ChromaDB collection
   - Split text for RAG implementation
   - Generate embeddings
   - Query documents with natural language questions

4. You can select different language models by uncommenting the appropriate lines:
   ```python
   # llm = init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct", model_provider="groq")
   # llm = init_chat_model("gpt-4.1-nano", model_provider="openai", temperature=0)
   # llm = init_chat_model("claude-3-7-sonnet-latest", model_provider="anthropic")
   ```

5. Adjust the RAG parameters in the notebook to optimize for your specific documents.

## Example Query

```python
question = "How can I measure a voltage differentially using ADCs in this micro?"
# The system will retrieve relevant context from the document and provide an answer
```

## Structured Response

The notebook also demonstrates how to get structured responses using Pydantic models:

```python
class ResponseFormatter(BaseModel):
    min: str = Field(description="value for the minimum")
    max: str = Field(description="value for the maximum")
    typical: str = Field(description="value for the typical")
    unit: str = Field(description="Unit of the value") 
    temperature: str = Field(description="Temperature of the value")
```

## Project Structure

```
AskYourDoc/
├── main.ipynb - Main notebook with the code
├── docs/ - Directory for PDF documents
│   ├── BOOSTXL-DRV8305EVM.pdf
│   ├── Infineon_IMZC120R017M2H.pdf
│   ├── LAUNCHXL-F28069M.pdf
│   └── ...
├── chroma/ - ChromaDB persistence directory
└── README.md - This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]