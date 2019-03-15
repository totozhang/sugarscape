class Sugar():

    def __init__(self, posx, posy, sugar):
        self.x = posx
        self.y = posy

        # sugar degree: 0 ~ 4
        self.sugar_uplimit = sugar
        self.sugar_current = sugar

    def degree_dec(self):
        self.sugar_current -= 1

    def degree_inc(self):
        self.sugar_current += 1

    def degree_filled(self):
        self.sugar_current = self.sugar_uplimit

    def degree_empty(self):
        self.sugar_current = 0



