from typing import Any
from mtoken import Token, TokenType, get_ident_type

__all__ = ["Lexer"]


class Lexer:
    char: Any
    position: int = 0
    read_position: int = 1

    def __init__(
        self,
        source_code: str,
    ):
        self.source_code = source_code
        self.char = source_code[0]

    def read_char(self) -> None:
        """We check the next character to ensure we didn't reach
        the end of the file, if we reach the eof we set the
        char to 0, otherwise we set the char to the read char. Then,
        we update the position to the read char, and increase"""

        # Checks if we reached the end of the input (source code)
        if self.read_position >= len(self.source_code):
            # We set this to 0 which is the ASCII code for NUL
            self.char = 0
        else:
            self.char = self.source_code[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def peek_char(self) -> str | int:
        """Peeks at the next character"""
        if self.read_position >= len(self.source_code):
            return 0
        return self.source_code[self.read_position]

    def next_token(self) -> Token:
        """Handles the logic of creating the tokes based on `self.char`"""
        token: Token
        self.skip_white_space()

        match self.char:
            case "=":
                # Looks ahead to se if there is another = if so then it must be an
                # TokenType.EQ mtoken, otherwise we simply return the singular `=`
                if self.peek_char() == "=":
                    ch = self.char
                    self.read_char()
                    literal = ch + self.char
                    token = Token(TokenType.EQ, literal)
                else:
                    token = Token(TokenType.ASSIGN, self.char)
            case "!":
                if self.peek_char() == "=":
                    ch = self.char
                    self.read_char()
                    literal = ch + self.char
                    token = Token(TokenType.NOT_EQ, literal)
                else:
                    token = Token(TokenType.BANG, self.char)
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
            case "-":
                token = Token(TokenType.MINUS, self.char)
            case "*":
                token = Token(TokenType.ASTERISK, self.char)
            case "/":
                token = Token(TokenType.SLASH, self.char)
            case "<":
                token = Token(TokenType.LT, self.char)
            case ">":
                token = Token(TokenType.GT, self.char)
            case 0:
                token = Token(TokenType.EOF, "")
            case _:
                if self.is_letter():
                    # Pretty self-explanatory we first read the read_identifier
                    # then we get the type of the identifier and lastly,
                    # we create the mtoken
                    literal = self.read_identifier()
                    token_type = get_ident_type(literal)
                    token = Token(token_type, literal)
                    return token
                elif self.char.isdigit():
                    token = Token(TokenType.INT, self.read_number())
                    return token
                else:
                    token = Token(TokenType.ILLEGAL, self.char)

        self.read_char()
        return token

    def skip_white_space(self) -> None:
        """
        Check if `self.char` is a white space includes \t \n \r and " ".

        Note: Because I'm dumb I used an if statement instead of a while
        loop, so it caused some issues.
        """
        while self.char and self.char.isspace():
            self.read_char()

    def read_identifier(self):
        """
        It loops through all consecutive letters, once there loop breaks
        we return the string of letters
        """
        # Starting position before the loops starts
        position = self.position
        while self.is_letter():
            # Since read char updates `self.position` we can use a combo of
            # the starting position and the `self.position` to get the word
            self.read_char()
        return self.source_code[position: self.position]

    def read_number(self):
        position = self.position

        while self.char.isdigit():
            self.read_char()

        return self.source_code[position: self.position]

    def is_letter(self) -> bool:
        return self.char.isalpha() or self.char == "_"
