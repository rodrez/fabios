import unittest

from fb_lexer import Lexer
from fb_token import TokenType


class TestLexerNextToken(unittest.TestCase):
    def test_next_token(self):
        token_types = [
            (TokenType.LET, "let"),
            (TokenType.IDENTIFIER, "five"),
            (TokenType.ASSIGN, "="),
            (TokenType.INT, "5"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.LET, "let"),
            (TokenType.IDENTIFIER, "ten"),
            (TokenType.ASSIGN, "="),
            (TokenType.INT, "10"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.LET, "let"),
            (TokenType.IDENTIFIER, "add"),
            (TokenType.ASSIGN, "="),
            (TokenType.FUNCTION, "fn"),
            (TokenType.LPAREN, "("),
            (TokenType.IDENTIFIER, "x"),
            (TokenType.COMMA, ","),
            (TokenType.IDENTIFIER, "y"),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.IDENTIFIER, "x"),
            (TokenType.PLUS, "+"),
            (TokenType.IDENTIFIER, "y"),
            (TokenType.RBRACE, "}"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.LET, "let"),
            (TokenType.IDENTIFIER, "result"),
            (TokenType.ASSIGN, "="),
            (TokenType.IDENTIFIER, "add"),
            (TokenType.LPAREN, "("),
            (TokenType.IDENTIFIER, "five"),
            (TokenType.COMMA, ","),
            (TokenType.IDENTIFIER, "ten"),
            (TokenType.RPAREN, ")"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.BANG, "!"),
            (TokenType.MINUS, "-"),
            (TokenType.SLASH, "/"),
            (TokenType.ASTERISK, "*"),
            (TokenType.INT, "5"),
            (TokenType.INT, "5"),
            (TokenType.LT, "<"),
            (TokenType.INT, "10"),
            (TokenType.GT, ">"),
            (TokenType.INT, "5"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.IF, "if"),
            (TokenType.LPAREN, "("),
            (TokenType.INT, "5"),
            (TokenType.LT, "<"),
            (TokenType.INT, "10"),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.RETURN, "return"),
            (TokenType.TRUE, "true"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.RBRACE, "}"),
            (TokenType.ELSE, "else"),
            (TokenType.LBRACE, "{"),
            (TokenType.RETURN, "return"),
            (TokenType.FALSE, "false"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.RBRACE, "}"),
            #
            (TokenType.INT, "10"),
            (TokenType.EQ, "=="),
            (TokenType.INT, "10"),
            (TokenType.INT, "10"),
            (TokenType.NOT_EQ, "!="),
            (TokenType.INT, "10"),
        ]

        source_code = """
let five = 5;
        let ten = 10;

        let add = fn(x,y) {
            x + y
        };

        let result = add(five, ten);

        !-/*5
        5 < 10  > 5;

        if (5 < 10){
            return true;
        } else {
            return false;
        }

        10 == 10
        10 != 10
        """

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
