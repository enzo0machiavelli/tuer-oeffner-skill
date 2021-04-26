from mycroft import MycroftSkill, intent_file_handler


class TuerOeffner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('oeffner.tuer.intent')
    def handle_oeffner_tuer(self, message):
        self.speak_dialog('oeffner.tuer')


def create_skill():
    return TuerOeffner()

