import keyboard

def saludo():
    print("¡Hola, Alejandro!")

keyboard.add_hotkey('ctrl+alt+h', saludo)

keyboard.wait('esc')  # El programa sigue corriendo hasta que presiones 'esc'
