

class Ascii:
    def __init__(self):
        self.rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

        self.paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

        self.scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

    def art(self, selection):
        if selection == 0:
            print(self.rock)
        elif selection == 1:
            print(self.paper)
        elif selection == 2:
            print(self.scissors)
