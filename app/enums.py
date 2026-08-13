from enum import Enum

class AnimeStatus(Enum):
    ONGOING = "Ongoing"
    COMPLETED = "Completed"

class APIKeyStatus(Enum):
    ACTIVE = "Active"
    REVOKED = "Revoked"
