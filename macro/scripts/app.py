import pyautogui
import time, sys
import keyboard
import threading


class TerminalApplication(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.working = False
        self.cursor = Cursor()
        self.stop_thread = False
        self.destination_position = None
        self.destination_time = 0
        self.pomin_reklame = False

    def run(self):

        user_input = input('Chcesz dodać przycisk "pomiń reklamę"? y/n?')
        if user_input == 'y':
            self.pomin_reklame = True

        user_input = input('Ustaw czas pomiędzy kólkiem, a strzałką i naciśnij ENTER: ')
        if user_input.isnumeric():
            self.destination_time_reklama_strzalka = int(user_input)

        if self.pomin_reklame:
            user_input = input('Ustaw czas pomiędzy strzałką, a pomin reklame i naciśnij ENTER: ')
            if user_input.isnumeric():
                self.destination_time_strzalka_pomin_reklame = int(user_input)

        user_input = input('Ustaw czas pomiędzy strzałką/"pomin reklame", a kółkiem i naciśnij ENTER: ')
        if user_input.isnumeric():
            self.destination_time_nastepna_reklama = int(user_input)


        input('Ustaw kursor w miejscu kółka i nacisnij ENTER')
        self.destination_position_reklama = self.cursor.get_current_cursor()


        input('Ustaw kursor w miejscu strzałki i nacisnij ENTER')
        self.destination_position_strzalka = self.cursor.get_current_cursor()

        if self.pomin_reklame:
            input('Ustaw kursor w miejscu pomin reklame i nacisnij ENTER')
            self.destination_position_pomin_reklame = self.cursor.get_current_cursor()


        while True:
            self.cursor.click_on_position(self.destination_position_reklama)
            time.sleep(self.destination_time_reklama_strzalka)
            self.cursor.click_on_position(self.destination_position_strzalka)
            if self.pomin_reklame:
                time.sleep(self.destination_time_strzalka_pomin_reklame)
                self.cursor.click_on_position(self.destination_position_pomin_reklame)
            time.sleep(self.destination_time_nastepna_reklama)

            if self.stop_thread:
                break


class Cursor:

    def __init__(self):
        self.position = [0, 0]
        self.clicked = False

    def set_position(self, position):
        pyautogui.moveTo(*position)

    def get_current_cursor(self):
        return pyautogui.position()

    def click_on_position(self, position):
        pyautogui.click(*position)

    def show_current_position(self):
        print(f'Current position of cursor: x: {pyautogui.position()[0]}, y: {pyautogui.position()[1]}')


def main():
    application = TerminalApplication()
    application.start()

    keyboard.wait('esc')
    application.stop_thread = True
    if application.is_alive():
        sys.exit()


if __name__ == '__main__':
    main()


