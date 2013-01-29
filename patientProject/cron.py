from django_cron import cronScheduler, Job
from patientProject.sendmessage import sendMessage

class CheckMail(Job):
    # run every 10 seconds
    run_every = 20
            
    def job(self):
            # This will be executed every 5 minutes
            sendMessage()

cronScheduler.register(CheckMail)