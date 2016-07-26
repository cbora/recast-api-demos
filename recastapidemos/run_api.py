import os
from samples.api import RecastApi
import recastapi




request_id = 5

if request_id == 0:
    raise Exception('request id not set')

r = RecastApi(request_id)

recastapi.ORCID_ID = os.environ.get('RECASTAPI_ORCID_ID', '')
recastapi.ACCESS_TOKEN = os.environ.get('RECASTAPI_ACCESS_TOKEN', '')

r.add_parameter_from_file('data/param_data.yaml') #'arg is hardcoded for testing purpose')

data = {'coordinates': [{'name': 'a', 'value': 1},
                        {'name': 'b', 'value': 2}],
        'basic': [{'filename': 'samples/file11.zip'},
                  {'filename': 'samples/file12.zip'}]
        }
r.printout()

r.add_point(data=data)

r.printout()

r.add_point_response('param_1', 'data/pointresponse.json', 'data/file11.zip')

r.add_basic_response('param_1', 'basic_0', 'data/basicresponse.json', 'data/file12.zip')


r.printout()
