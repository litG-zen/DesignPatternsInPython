from abc import ABC, abstractmethod


class SendNotification(ABC):
    @abstractmethod
    def send(self, recipient:str, message:str, body:str) -> None:
        pass


class EmailNotification(SendNotification):
    def send(self, recipient:str, message:str, body:str) -> None:
        print(f"Sending email to {recipient} with subject '{message}' and body '{body}'")   

class SESEmailService:
    def send_email(self, recipient:str, message:str, body:str) -> None:
        print(f"Sending email to {recipient} with subject '{message}' and body '{body}'")   


class OrderService:
    def __init__(self,email_service:SendNotification):
        self._email_service = email_service
    
    def create_order(self,resp,subject,body):
        self._email_service.send(resp, subject, body)
    

custom_email_notif = EmailNotification()
order_service = OrderService(custom_email_notif)
order_service.create_order('lit@gmail.com','order created', 'order has been placed')

#Now in order to integrate the send_email method od SESEmailService class, we have to create an adapter which can mimich
# like SendNotification Abstract class dnd implements its send function.

class SESEmailServiceAdapter(SendNotification):
    def __init__(self, ses_service: SESEmailService):
        self._email_service = SESEmailService

    def send(self, recipient:str, message:str, body:str) -> None:
        self._email_service.send_email(recipient, message, body)


ses_email_notif = SESEmailServiceAdapter(SESEmailService)
order_service_2 = OrderService(ses_email_notif)
order_service.create_order('lit@gmail.com','order created using ses', 'order has been placed')
