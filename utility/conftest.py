import json
import pytest
import requests

@pytest.fixture()
def times():
    with open("../data/time.json") as timevalues:
        values= json.loads(timevalues.read())
        final=""
        if len(values)>10:
            print("The max limit of values is 10 for the time input")
        else:
            for k,v in values.items():
                final=final+ v +","
            return (final[:-1])

@pytest.fixture()
def geturl():
    with open("../data/baseurl.json") as urlvalue:
        convert_to_json=  json.loads(urlvalue.read())
        url=convert_to_json["url"]
        return url

@pytest.fixture()
def getsatelliteid(geturl):
    satelliteid = requests.get(geturl+"satellites")
    satelliteid.json()
    satelliteid=str((satelliteid.json())[0]["id"])
    return satelliteid


@pytest.fixture()
def millisec():
    with open("../data/time.json") as timevalues:
        value=(json.loads(timevalues.read()))
        return value


@pytest.fixture()
def numberoftimes():
    with open("../data/time.json") as timevalues:
        values= json.loads(timevalues.read())
    return (len(values))