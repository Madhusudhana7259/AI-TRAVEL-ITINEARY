from langchain_core.messages import HumanMessage, AIMessage
from src.chain.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""

        logger.info("TravelPlanner initialized")
    
    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info(f"City set successfully: {city}")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException("Failed to set city", e)
    
    def set_interests(self, interests: str):
        try:
            self.interests = [i.strip() for i in interests.split(",")]
            self.messages.append(HumanMessage(content=interests))
            logger.info(f"Interests set successfully: {interests}")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException("Failed to set interests", e)
    
    def create_itinerary(self):
        try:
            logger.info("Generating itinerary for %s with interests %s", self.city, self.interests)
            itinerary = generate_itinerary(self.city, self.interests)
            self.itineary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info(f"Itinerary created successfully: {itinerary}")
            return self.itineary
        except Exception as e:
            logger.error(f"Error creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)