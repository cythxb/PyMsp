import hashlib
from random import randint


class TicketGenerator:
    markingID = randint(0,1000)
    def headerTicket(ticket : str):
        return ticket + TicketGenerator.getMarkingId()
    def getMarkingId():
        TicketGenerator.markingID += 1
        return str(hashlib.md5(str(TicketGenerator.markingID).encode('utf-8')).hexdigest()) + str.encode(str(TicketGenerator.markingID)).hex().replace("-", "")