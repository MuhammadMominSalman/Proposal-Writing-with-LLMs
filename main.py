import os
from langchain import OpenAI
from langchain.chains import SimpleChain
from langchain.prompts import PromptTemplate
from langchain import OpenAI
from config import OPENAI_API_KEY

# Initialize the language model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Define prompts for different stages of proposal writing
idea_prompt = PromptTemplate(input_variables=["topic"], template="Generate a project proposal for {topic}")
structure_prompt = PromptTemplate(input_variables=["idea"], template="Structure the following idea into sections: {idea}")
refine_prompt = PromptTemplate(input_variables=["structure"], template="Refine the following proposal structure: {structure}")

# Create chains
idea_generation_chain = SimpleChain(prompt_template=idea_prompt, llm=llm)
structure_chain = SimpleChain(prompt_template=structure_prompt, llm=llm)
refinement_chain = SimpleChain(prompt_template=refine_prompt, llm=llm)

# Combine chains
proposal_chain = idea_generation_chain | structure_chain | refinement_chain