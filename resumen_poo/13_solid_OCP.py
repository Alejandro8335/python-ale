
#ocp,principio de abierto/cerrado
#open/closed principle

class Notificador:
    def __init__(self,usuario,mensaje):
        self.ususario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"enviado mensaje a {self.ususario}:{self.mensaje}")
        
class NotificadorSms(Notificador):
    def notificar(self):
        print(f"enviado sms a {self.ususario}:{self.mensaje}")

usuario = input("para quien es el mensaje:  ")
mensaje = input("mensaje:  ")
notificador = NotificadorEmail(usuario,mensaje)
notificador.notificar()

#Las clases, módulos y funciones deben estar abiertas para la extensión, pero cerradas para la modificación.

#Esto significa que, cuando necesites agregar nuevas funcionalidades a tu código, 
#deberías hacerlo sin cambiar el código existente. En lugar de modificar una clase directamente, 
#puedes extender su comportamiento utilizando herencia o implementando nuevas clases que sigan la misma interfaz.