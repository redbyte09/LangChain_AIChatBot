# langchain_helper.py

import os
from langchain_community.llms import Cohere
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory



# You can hardcode or use os.getenv("COHERE_API_KEY") if using .env
def get_chat_chain():
    llm = Cohere(
        cohere_api_key=os.getenv("COHERE_API_KEY", "EEHgpuTUanIxAvCpbvMN7nlmVZBuOBiK7RZ8T8hg"),
        model="command-light",  # use light free-tier model
        temperature=0.7
    )

    memory = ConversationBufferMemory()

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    return conversation
