from django_cron import cronScheduler, Job
from functions.sendmessage import sendMessage

class CheckMail(Job):
    # run every 10 seconds
    run_every = 2
            
    def job(self):
            # This will be executed every 5 minutes
            #sendMessage()
            print "Hello"

cronScheduler.register(CheckMail)
