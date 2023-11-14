import winsound as wns, time
from colorama import init, Fore, Back

init(autoreset=True)
cy = Fore.CYAN
cy2 = Fore.BLUE

gn = Fore.GREEN
yl = Fore.YELLOW

class sound:
    def SystemAsterisk(self):
        print(f"Playing {cy}\"SystemAsterisk\" : ")
        start = time.time()
        wns.PlaySound("SystemAsterisk", wns.SND_ALIAS)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{cy2} audio : {elapsed:2F} ms\n")
        time.sleep(1)
        
    def SystemExclamation(self):
        print(f"Playing {cy}\"SystemExclamation\" : ")
        start = time.time()
        wns.PlaySound("SystemExclamation", wns.SND_ALIAS)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{cy2} audio : {elapsed:2F} ms\n")
        time.sleep(1)

    def SystemExit(self):
        print(f"Playing {cy}\"SystemExit\" : ")
        start = time.time()
        wns.PlaySound("SystemExit", wns.SND_ALIAS)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{cy2} audio : {elapsed:2F} ms\n")
        time.sleep(1)
        
    def SystemHand(self):
        print(f"Playing {cy}\"SystemHand\" : ")
        start = time.time()
        wns.PlaySound("SystemHand", wns.SND_ALIAS)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{cy2} audio : {elapsed:2F} ms\n")
        time.sleep(1)

    def SystemQuestion(self):
        print(f"Playing {cy}\"SystemQuestion\" : ")
        start = time.time()
        wns.PlaySound("SystemQuestion", wns.SND_ALIAS)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{cy2} audio : {elapsed:2F} ms\n")
        time.sleep(1)

class msbeep:
    # Asterisk
    def Asterisk(self):
        print(f"Playing {gn}\"MB_ICONASTERISK\" : ")
        start = time.time()
        wns.MessageBeep(wns.MB_ICONASTERISK)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{yl} audio : {elapsed:2F} ms\n")
        time.sleep(1)

    #   Exclamation
    def Exclamation(self):
        print(f"Playing {gn}\"MB_ICONEXCLAMATION\" : ")
        start = time.time()
        wns.MessageBeep(wns.MB_ICONEXCLAMATION)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{yl} audio : {elapsed:2F} ms\n")
        time.sleep(1)

    #	Critical Stop
    def Critical_stop(self):
        print(f"Playing {gn}\"MB_ICONHAND\" : ")
        start = time.time()
        wns.MessageBeep(wns.MB_ICONHAND)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{yl} audio : {elapsed:2F} ms\n")
        time.sleep(1)
    
    #	Question
    def qustion(self):
        print(f"Playing {gn}\"MB_ICONQUESTION\" : ")
        start = time.time()
        wns.MessageBeep(wns.MB_ICONQUESTION)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{yl} audio : {elapsed:2F} ms\n")
        time.sleep(1)

    #	System Default
    def deafult(self):
        print(f"Playing {gn}\"MB_OK\" : ")
        start = time.time()
        wns.MessageBeep(wns.MB_OK)
        end = time.time()
        elapsed = (end - start)*1000
        print(f"{yl} audio : {elapsed:2F} ms\n")
        time.sleep(1)

class main:
    def winsound(self):
        s = sound()
        # attr = dir(s)
        # funcs = [attr for attr in attr if callable(getattr(s, attr))]

        # for i in funcs:
        #     method = getattr(s, i)
        #     if callable(method):
        #         method()
                
        s.SystemAsterisk()
        s.SystemExclamation()
        s.SystemExit()
        s.SystemHand()
        s.SystemQuestion()
        
    def ms_beep(self):
        s = msbeep()
        # attr = dir(s)
        # funcs = [attr for attr in attr if callable(getattr(s, attr))]

        # for i in funcs:
        #     method = getattr(s, i)
        #     if callable(method):
        #         method()
        
        s.Asterisk()
        s.Exclamation()
        s.Critical_stop()
        s.qustion()
        s.deafult()

def run():
    fn = main()
    # attr = dir(fn)
    # funcs = [attr for attr in attr if callable(getattr(fn, attr))]
    # for i in funcs:
    #     method = getattr(fn, i)
    #     if callable(method):
    #         method()
    fn.winsound()
    fn.ms_beep()
    
run()