class wifidevice:
    def wifi(self):
        print("wifi connected")
class voiceassistant:
    def voice(self):
        print("voice control active")
class smartspeaker(wifidevice,voiceassistant):
    def display(self):
        print("smart speaker ready")
s = smartspeaker()
s.wifi()
s.voice()
s.display()
