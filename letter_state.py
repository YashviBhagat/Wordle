class LetterState:
    def __init__(self,character):
        self.character = character
        self.is_in_word = False
        self.is_in_position = False
    def __repr__(self) -> str:
        return f"[{self.character} is_in_word:{self.is_in_word} is_in_position:{self.is_in_position}]"