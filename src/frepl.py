from flexer import Lexer, TokenType


PROMPT = ">> "


def start(input_stream, output_stream):
    """
    Goes over the input line, if theres no line we simply
    return. If there is a line, we pass the line to the Lexer
    then we loop until we find EOF which should be the last
    space, for each token found we return the type: literal
    """
    for line in input_stream:
        output_stream.write(PROMPT)
        line = line.strip()
        if not line:
            return
        print(line)
        lexer = Lexer(line)

        tok = lexer.next_token()
        while tok.token_type != TokenType.EOF:
            output_stream.write(str(tok) + "\n")
            tok = lexer.next_token()
