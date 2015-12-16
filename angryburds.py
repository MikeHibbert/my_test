class Burd(object):
    def __init__(self, call=None, wing_sound=None):
        self.call = call or "Cheep Cheep!"
        self.wing_sound = wing_sound or "flap flap!"

    def do_call(self):
        print self.call

    def do_flap(self):
        print self.wing_sound


