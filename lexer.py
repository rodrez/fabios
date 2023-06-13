from .token import Token, TokenType
from ctypes import c_ubyte


class Lexer:
    def __init__(
        self, input: str, position: int, readPosition: int, ch: c_ubyte
    ) -> None:
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
        pass

    def read_char(self):
        pass


def test_next_token():
    token_types = [
        (TokenType.ASSIGN, "="),
        (TokenType.PLUS, "+"),
        (TokenType.ILLEGAL, "ILLEGAL"),
        (TokenType.EOF, "EOF"),
        # Identifiers + literals
        (TokenType.IDENTIFIER, "IDENTIFIER"),
        (TokenType.INT, "INT"),
        # Operators
        (TokenType.ASSIGN, ","),
        (TokenType.PLUS, "+"),
        # Delimeters
        (TokenType.COMMA, ","),
        (TokenType.SEMICOLON, ";"),
        (TokenType.LPAREN, "("),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RBRACE, "}"),
        # Keywords
        (TokenType.FUNCTION, "FUNCTION"),
        (TokenType.LET, "LET"),
    ]
