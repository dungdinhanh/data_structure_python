class Word:
    def __int__(self):
        self.eng = None
        self.vi = None

    def input_word(self, english, vietnam):
        self.eng = english
        self.vi  = vietnam

    def compare_function(self, word):
        return self.eng - word.eng

    def __str__(self):
        return self.eng + " : " + self.vi

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return self.eng == other.eng

    def __lt__(self, other):
        if self is other:
            return False
        elif type(self) != type(other):
            return False
        return self.eng < other.eng
