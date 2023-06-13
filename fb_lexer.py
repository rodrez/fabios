from typing import Any
from .fb_token import Token, TokenType


class Lexer:
    char: Any
    position: int = 0
    readPosition: int = 1

    def __init__(
        self,
        source_code: str,
    ):
        """
        Parameters
        ----------
        input
            Source code
        position
            Current position in the source code
        readPosition
            Character after current
        character
            Current character
        """
        self.source_code = source_code
        self.char = source_code[0]

    def read_char(self):
        """We check the next character to ensure we didn't reached
        reach the end of the file, if we reach the eof we set the
        char to 0, otherwise we set the char to the read char. Then,
        we update the position to the read char, and increase"""

        # Checks if we reached the end of the input (source code)
        if self.readPosition >= len(self.source_code):
            # We set this to 0 which is the ASCII code for NUL
            self.char = 0
        else:
            self.char = self.source_code[self.readPosition]

        self.position = self.readPosition
        self.readPosition += 1

    def next_token(self) -> Token:
        token: Token = Token(TokenType.EOF, "")
        match self.char:
            case "=":
                token = Token(TokenType.ASSIGN, self.char)
            case ";":
                token = Token(TokenType.SEMICOLON, self.char)
            case "(":
                token = Token(TokenType.LPAREN, self.char)
            case ")":
                token = Token(TokenType.RPAREN, self.char)
            case "{":
                token = Token(TokenType.LBRACE, self.char)
            case "}":
                token = Token(TokenType.RBRACE, self.char)
            case ",":
                token = Token(TokenType.COMMA, self.char)
            case "+":
                token = Token(TokenType.PLUS, self.char)
            case 0:
                token = Token(TokenType.EOF, "")

        self.read_char()
        return token
