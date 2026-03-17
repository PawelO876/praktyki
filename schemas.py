from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import List

# --- Enum dla ról w konwersacji ---
class MessageRole(str, Enum):
    """Enumeration dla ról w konwersacji"""
    SYSTEM = "system
