import json
from utils import validateUserInput
from trainapi import getLiveJourneys

origin, calling_at = validateUserInput()
journeys = getLiveJourneys(origin, calling_at)

print(journeys)

