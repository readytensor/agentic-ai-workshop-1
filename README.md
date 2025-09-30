# Agentic AI Workshop 1: Building AI Apps with RAG and LLM Workflows

## Workshop Summary

This hands-on 1-hour workshop introduces participants to building intelligent AI applications using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG). Attendees will progress from basic LLM API calls to creating a fully functional RAG-based chatbot that can answer questions using custom documents. The workshop emphasizes practical coding with immediate results, using popular tools like OpenAI's API, ChromaDB, and Gradio for interactive interfaces.

**Target Audience:** Developers and technical professionals with basic Python knowledge who want to understand and build agentic AI applications.

**Key Takeaways:**

- Understand core concepts of agentic AI and prompt engineering
- Make API calls to LLMs for various tasks (text, image, audio generation)
- Learn how embeddings and vector databases enable semantic search
- Build a complete RAG-based chatbot from scratch

---

## Workshop Outline

### **Part 1: Introduction (10-12 minutes)**

**Slides covering:**

- What is Agentic AI?
- Basics of Prompt Engineering
- LLM Workflows vs Multi-Agent Systems
- Understanding Embeddings and Vector Databases
- Introduction to Retrieval-Augmented Generation (RAG)

---

### **Part 2: Coding Session - Building Blocks (40-45 minutes)**

#### **Notebook 1: Basic LLM API Interactions (15-18 minutes)**

1. Basic API call to an LLM - text in, text out
2. Image generation example - text to image
3. Sound generation example - text to audio
4. Create a Gradio UI for interactive testing
5. Implement streaming output for real-time responses
6. Build a multi-turn chat conversation

**Technologies:** OpenAI Python SDK, Gradio

---

#### **Notebook 2: Embeddings and Similarity Search (8-10 minutes)**

1. Generate embeddings for different documents
2. Calculate cosine similarity between documents
3. Find the most similar documents to a query (without vector DB yet)

**Technologies:** OpenAI Embeddings API

---

#### **Notebook 3: RAG-Based Chatbot with Vector DB (15-18 minutes)**

1. Ingest documents into ChromaDB (using 5 Ready Tensor publications)
2. Implement semantic document retrieval
3. Build a complete RAG pipeline
4. Deploy in a Gradio Chat UI

**Technologies:** ChromaDB, OpenAI API, Gradio

---

### **Part 3: Wrap-Up (5 minutes)**

**Slides covering:**

- Summary of what we covered
- Limitations and cautions of current approaches
- Next steps and advanced topics to explore
- Resources for continued learning

---

## Technical Stack

- **LLM Provider:** OpenAI (GPT-4/GPT-3.5)
- **Embeddings:** OpenAI `text-embedding-3-small`
- **Vector Database:** ChromaDB
- **UI Framework:** Gradio
- **Development Environment:** Jupyter Notebooks
- **Language:** Python 3.11+

---

## Pre-Workshop Requirements

Attendees should:

- Have Python 3.11 or higher installed
- Obtain an OpenAI API key
- Install required packages: `openai`, `chromadb`, `gradio`, `numpy`
- Have basic familiarity with Python and Jupyter notebooks

---

# Setup Instructions

Follow these steps to get your environment ready for the workshop.

### 1. Clone and enter the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create and activate a virtual environment

It’s best to isolate workshop dependencies. You can use either `venv` or `conda`.

**Using venv (Python 3.9+ recommended):**

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

**Using conda:**

```bash
conda create -n agentic_ai python=3.11 -y
conda activate agentic_ai
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

You need an API key with access to GPT-4o models. Set it as an environment variable:

**macOS / Linux:**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows (Powershell):**

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Restart your terminal (or run `refreshenv` in Powershell) so the variable is available.

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open one of the notebooks (`part1_basic_llm.ipynb`, `part2_embeddings_cosine.ipynb`, or `part3_rag_chromadb.ipynb`) to get started.

---

⚡ **Tip:** If you run into dependency conflicts, you can upgrade packages individually, e.g.:

```bash
pip install --upgrade openai gradio chromadb
```

---
