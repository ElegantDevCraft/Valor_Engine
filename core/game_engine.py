from rich.logging import RichHandler
import logging
import keyboard

# Central game mechanics and state management

logging.basicConfig(level="INFO", handlers=[RichHandler()])
logger = logging.getLogger("game_engine")