from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=GROQ_API_KEY,
)

itineary_prompt = ChatPromptTemplate([
    ("system", "You are a helpful travel assistant. Create a day trip itineray for {city} based on the user interest: {interests}. Provide a brief, bulleted itineray"),
    ("human", "Create a itinery for a day trip")
])

def generate_itinerary(city:str, interests:list[str]) -> str:
    prompt = itineary_prompt.format_messages(city=city, interests=", ".join(interests))
    response = llm.invoke(prompt)
    return response.content