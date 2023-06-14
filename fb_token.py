from enum import Enum

"""
This file holds everything related to the Token. We can create new TokenTypes
by simply adding the to our `TokenTyp` enum.
"""


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literals
    IDENTIFIER = "IDENTIFIER"
    INT = "INT"

    # Operators
    ASSIGN = "="
    PLUS = "+"

    # Delimeters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords

    FUNCTION = "FUNCTION"
    LET = "LET"


KEYWORDS: dict[str, TokenType] = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
}


def get_ident_type(ident: str) -> TokenType:
    """
    Find the identifier in the KEYWORDS constant, if there is
    no identifier, return TokenType.IDENTIFIER.
    """
    return KEYWORDS.get(ident, TokenType.IDENTIFIER)


class Token:
    def __init__(self, token_type: TokenType, literal: str) -> None:
        self.token_type = token_type
        self.literal = literal
