
import requests, json

app_id = "bb807574"
app_key = "ad433d69a3c31ab4ed71ad6861470fc8"
transportapi = "https://transportapi.com/v3"

extractionList = ["expected_departure_time", "platform", "status"]


def getLiveJourneys(origin, calling_at): 
    queryString = buildQueryString(origin, calling_at)

    response = requests.get(transportapi + queryString)

    journeys = json.loads(response.text)
    departures = Departures(journeys["departures"]["all"])

    return departures.extract(extractionList)


def buildQueryString(origin, calling_at):
    return (
        '/uk/train/station/{}/live.json?'
        'app_id={}&'
        'app_key={}&'
        'darwin=false&'
        'calling_at={}&'
        'train_status=passenger'
    ).format(origin, app_id, app_key, calling_at)

class Departures:
    def __init__(self, departures):
        self.departures = departures

    def extract(self, filters):
        allResponses = []
        for departure in self.departures:
            response = {}
            for filter in filters:
                response[filter] = departure.get(filter)
            allResponses.append(response)
        return allResponses

