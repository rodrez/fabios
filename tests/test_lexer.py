from ..fb_token import TokenType
from ..fb_lexer import Lexer
import unittest


class TestLexerNextToken(unittest.TestCase):
    def test_next_token(self):
        token_types = [
            (TokenType.ASSIGN, "="),
            (TokenType.PLUS, "+"),
            (TokenType.LPAREN, "("),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.RBRACE, "}"),
            (TokenType.COMMA, ","),
            (TokenType.SEMICOLON, ";"),
        ]

        source_code = "=+(){},;"

        lexer = Lexer(source_code)
        for tok in token_types:
            lt = lexer.next_token()

            expected_type, expected_literal = tok

            self.assertEqual(
                lt.token_type,
                expected_type,
                f"Wrong token type {lt.token_type}, expected {expected_type}",
            )

            self.assertEqual(
                lt.literal,
                expected_literal,
                f"Wrong token literal {lt.literal}, expected {expected_literal}",
            )

    def test_true(self):
        self.assertTrue(1 == 1)


if __name__ == "__main__":
    unittest.main()
