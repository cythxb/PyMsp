import pyamf
from pyamf import remoting
from pyamf.flex import messaging
import requests

from AMF import AMF
from SessionUtils import SessionUtils

class SessionID:
    def GetSessionId():
        AMF.GetEndpointForServer("FR")
        createos = AMF.SendAMF("MovieStarPlanet.WebService.Os.AMFOs.CreateOsRef", [])
        runos = AMF.SendAMF("MovieStarPlanet.WebService.Os.AMFOs.RunOsCheck", [ str(createos["RefId"]), SessionUtils.MSP_SESSION_DICTIONARY[createos["TjData"]]], False)
        resp_msg = remoting.decode(runos)
        return str(resp_msg.bodies[0][1]).replace("<Response status=/onResult>'", "").replace("'</Response>", "")
