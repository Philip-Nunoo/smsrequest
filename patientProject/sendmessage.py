from patientProject.models import Message, Hospital, Patient, MessageLog
import datetime

key = "22ccfebddfe274033b29"
url = "http://bulk.mnotification.com/smsapi"

def sendMessage():       
    # Get all messages with sending_at_date == today()
    ### Send Message to users with messages
    ### update new send date to 
    messages_object = Message.objects.filter(start_at_date = datetime.date.today())
    
    if (messages_object):
        for message in messages_object:
            if message.active:
                message_content = message.message_content;
                phone_number = message.receipient_name.telephone_number
                sender_id = message.receipient_name.hospital_id
                
                get_data = {
                    'key': key, 
                    'to': phone_number, 
                    'msg': message_content, 
                    'sender_id': sender_id
                }
                
                #requests.get(url, params = get_data)        # This line sends the message to mnotify                
                '''
                    creating a log of message that was sent
                '''
                patient = Patient.objects.get(id = message.receipient_name.id)
                message_log = MessageLog.objects.create( message = message, patient = patient)
                
            if message.message_frequency == "daily":
                #message.start_at_date = message.start_at_date + datetime.timedelta(days=1)
                print "Daily message"
            if message.message_frequency == "weekly":
                #message.start_at_date = message.start_at_date + datetime.timedelta(days=7)
                print "Weekly Message"
            if message.message_frequency == "monthly":
                #message.start_at_date = message.start_at_date + datetime.timedelta(days=30)
                print "Monthly Message"
            if message.message_frequency == "specify":
                print "Specific date set"
            #if message.start_at_date > message.end_at_date: # if message exceeds ending date active = False
             #   message.active = False
                    
    #else:
    #    print "no message to send today"
        
def sendMessageNow(message, receipient_id):
    #save message content
    message_content = message
    
    #get the number of the receipient from the id
    patient = Patient.objects.get(id = receipient_id)
    phone_number = patient.telephone_number
    
    #get the hospital the receipient is registered to from the receipient_id variable
    sender_id = patient.hospital_id.hospital_name
    #store the message in the message variable
    get_data = {
        'key': key, 
        'to': phone_number, 
        'msg': message_content, 
        'sender_id': sender_id
    }

    ##requests.get(url, params = get_data)
    print "message sent to user"
    