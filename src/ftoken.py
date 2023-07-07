from dataclasses import dataclass
from enum import Enum

"""
This file holds everything related to the Token. We can create new TokenTypes
by simply adding the to our `TokenTyp` enum.
"""

__all__ = ["TokenType", "Token", "get_ident_type"]


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literals
    IDENTIFIER = "IDENTIFIER"
    INT = "INT"

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    LT = "<"
    GT = ">"

    EQ = "=="
    NOT_EQ = "!="

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    IF = "IF"
    ELSE = "ELSE"
    TRUE = "TRUE"
    FALSE = "FALSE"
    RETURN = "RETURN"


KEYWORDS: dict[str, TokenType] = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "return": TokenType.RETURN,
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

    def __str__(self) -> str:
        return f"Type: {self.token_type}".ljust(30) + f"Literal: {self.literal}"
