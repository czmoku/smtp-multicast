import aiosmtpd.controller
from smtplib import SMTP as Client
import os
import signal
import time

appPort = int(os.getenv("SMTP_MULTICAST_PORT") or "1025")
firstDestHostname = os.getenv("FIRST_DESTINATION_HOSTNAME") or "localhost"
firstDestPort = int(os.getenv("FIRST_DESTINATION_PORT") or "1025")
secondDestHostname = os.getenv("SECOND_DESTINATION_HOSTNAME") or "localhost"
secondDestPort = int(os.getenv("SECOND_DESTINATION_PORT") or "1025")


if (secondDestHostname == "localhost" and secondDestPort == appPort) or (firstDestHostname == "localhost" and firstDestPort == appPort):
    raise Exception("Cannot set destination server port same as server started, that makes infinity loop")

class SMTPMulticastHandler:
    async def handle_DATA(self, server, session, envelope):
        self.send(firstDestHostname, firstDestPort, envelope, "First destination server ({}:{})".format(firstDestHostname, firstDestPort))
        self.send(secondDestHostname, secondDestPort, envelope, "Second destination server ({}:{})".format(secondDestHostname, secondDestPort))
        return '250 OK'

    def send(self, hostname, port, envelope, name):
        try:
            firstDestClient = Client(hostname, port)
            firstDestClient.sendmail(envelope.mail_from, envelope.rcpt_tos, envelope.content)
        except:
            print("Problem during sending to {}, skipping".format(name))

handler = SMTPMulticastHandler()
server = aiosmtpd.controller.Controller(handler, hostname="0.0.0.0", port=appPort)
server.start()
print("Multicast SMTP proxy started on port {}\n".format(appPort))
server._thread.join()
print("Stopping server")
server.stop()