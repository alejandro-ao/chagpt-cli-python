from dotenv import load_dotenv
import os

from langchain.memory import ConversationEntityMemory
from langchain.chains import ConversationChain
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.llms import OpenAI

load_dotenv()

# Load the OpenAI API key from the environment variable
if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
    print("OPENAI_API_KEY is not set")
    exit(1)
else:
    print("OPENAI_API_KEY is set")

llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=ConversationEntityMemory(llm=llm)
)

print("Hello, I am ChatGPT CLI!")

while True:
    user_input = input("> ")

    ai_response = conversation.predict(input=user_input)

    print("\nAssistant:\n", ai_response, "\n")
