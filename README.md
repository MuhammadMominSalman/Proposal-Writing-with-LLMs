# LangChain Proposal Writing Assistant

## Overview

The **LangChain Proposal Writing Assistant** is a Python-based project that leverages the power of LangChain and language models to streamline the process of generating, structuring, and refining proposals. Whether you are working on a business proposal, research grant, or project plan, this tool helps you produce well-organized and coherent content with minimal effort.

## Features

- **Automated Proposal Generation**: Generate proposal content based on a given topic.
- **Content Structuring**: Organize the generated content into sections such as Introduction, Objectives, Methodology, and more.
- **Content Refinement**: Refine the proposal for clarity and coherence.
- **Customizable**: Tailor the prompts and structure to fit specific types of proposals.
- **User Interface Options**: Run the tool via a simple command-line interface (CLI) or a web-based interface using Streamlit.

## Installation

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key (or another language model API key)
- Optional: Streamlit for a web-based interface

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/langchain_proposal.git
    cd langchain_proposal
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv langchain_proposal_env
    source langchain_proposal_env/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API key**:
    - Create a `.env` file in the root of the project directory and add your API key:
      ```bash
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

### Web Interface (Streamlit)

1. **Install Streamlit** (if not installed):
    ```bash
    pip install streamlit
    ```

2. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

3. **Access the web app**:
    - Open your web browser and navigate to the provided local URL (e.g., `http://localhost:8501`).

4. **Generate a proposal**:
    - Enter your topic and click "Generate Proposal" to get started.

## Customization

### Modifying the Proposal Structure

To customize the structure of the proposals, you can modify the prompts in the `proposal_chain.py` file. Add new sections, change existing ones, or adjust the language model's behavior by editing the prompt templates.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.
