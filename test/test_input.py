import json
import requests
import io


class Satellites():
    "Test Satellite"


def test_get_position_two_times_miles(geturl, getsatelliteid, times, numberoftimes,millisec):
    "position of two satellites in two times and units as miles"
    response = requests.get(geturl + "satellites/" + getsatelliteid + "/positions",
                            params={"timestamps": times,
                                    "units": "miles"})
    # print(json.dumps(response.json(),indent=5))

    for i in range(numberoftimes):
        assert response.status_code == 200
        assert (response.json())[i]["id"] == 25544
        assert (response.json())[i]["units"] == "miles"
        assert (response.json())[i]["name"] == "iss"
        assert (response.json())[i]["timestamp"] == int(millisec["time"+ str(i+1)])


def test_get_position_two_times_kms(geturl, getsatelliteid, times, numberoftimes):
    "position of two satellites in two times and units as kms"
    response = requests.get(geturl + "satellites/" + getsatelliteid + "/positions",
                            params={"timestamps": times})
    #  print(json.dumps(response.json(),indent=5))

    assert response.status_code == 200
    for i in range(numberoftimes):
        assert (response.json())[i]["id"] == 25544
        assert (response.json())[i]["units"] == "kilometers"
        assert (response.json())[i]["name"] == "iss"


def test_get_tles_json(geturl, getsatelliteid):
    "check tles data in JSON format"
    response = requests.get(geturl + "satellites/" + getsatelliteid + "/tles")
    print(json.dumps(response.json(),indent=5))
    assert response.status_code == 200
    assert (response.json())["id"] == '25544'
    assert (response.json())["name"] == "iss"


def test_get_tles_text(geturl, getsatelliteid, numberoftimes):
    "check tles data in text format"
    response = requests.get(geturl + "satellites/" + getsatelliteid + "/tles",
                            params={"format": "text"})

    finalresponse = (io.StringIO(response.text)).readlines()
    assert (len(finalresponse)) == (numberoftimes) + 1
    if "ISS" in (finalresponse[0]):
        print("ISS is present in the first line of response")
    for i in range(1, len(finalresponse)):
        if getsatelliteid in finalresponse[i]:
            print("satellite ID is present in line number", i + 1)
