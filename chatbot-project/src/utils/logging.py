import logging

# Configure logging
logging.basicConfig(
    filename='chatbot_interactions.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_interaction(user_input, bot_response):
    logging.info(f'User Input: {user_input}')
    logging.info(f'Bot Response: {bot_response}')