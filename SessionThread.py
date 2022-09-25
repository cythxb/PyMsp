import threading
import time
from SessionID import SessionID
from AMF import AMF
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      while True:
         time.sleep(300)
         AMF.SessionId = SessionID.GetSessionId()
class myThread1 (threading.Thread):
   loginResps = {}
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      while True:
         AMF.GetEndpointForServer("DE")
         myThread1.loginResps["DE"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("US")
         myThread1.loginResps["US"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("DK")
         myThread1.loginResps["DK"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("NO")
         myThread1.loginResps["NO"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("SE")
         myThread1.loginResps["SE"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("FI")
         myThread1.loginResps["FI"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("NL")
         myThread1.loginResps["NL"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("GB")
         myThread1.loginResps["GB"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("PL")
         myThread1.loginResps["PL"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("FR")
         myThread1.loginResps["FR"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("TR")
         myThread1.loginResps["TR"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("AU")
         myThread1.loginResps["AU"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("CA")
         myThread1.loginResps["CA"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("IE")
         myThread1.loginResps["IE"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("NZ")
         myThread1.loginResps["NZ"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         AMF.GetEndpointForServer("ES")
         myThread1.loginResps["ES"] = AMF.SendAMF("MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", [ "WhyAreYouReadingThis ?", "google123n", None, None, None, "MSP1-Standalone:XXXXXX"])
         time.sleep(10800)