from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    print("Langchain Basics")

    summary_template = """
        give the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": "Elon Musk"})

    print(res)
