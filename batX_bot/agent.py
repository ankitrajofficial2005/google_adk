from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
root_agent = Agent(
    # model='gemini-3.5-flash',
    
    model="openrouter/openrouter/free",
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    generate_content_config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=800,
    )
)
# litellm is a library thats lets your code talk to 100+ llm providers (open ai, anthropic, ollama and more) through
# one standard interface , so switching models is one-line change.
