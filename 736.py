class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(tokens):
            token = tokens.pop(0)
            if token == '(':
                expr = []
                while tokens[0] != ')':
                    expr.append(parse(tokens))
                tokens.pop(0)  # remove ')'
                return expr
            elif token == ')':
                return None
            else:
                return token

        def tokenize(expr):
            expr = expr.replace('(', ' ( ').replace(')', ' ) ')
            return expr.split()

        def eval_expr(expr, scope):
            if isinstance(expr, str):
                if expr.lstrip('-').isdigit():
                    return int(expr)
                for s in reversed(scope):
                    if expr in s:
                        return s[expr]
            elif expr[0] == 'add':
                return eval_expr(expr[1], scope) + eval_expr(expr[2], scope)
            elif expr[0] == 'mult':
                return eval_expr(expr[1], scope) * eval_expr(expr[2], scope)
            elif expr[0] == 'let':
                new_scope = scope + [{}]
                for i in range(1, len(expr) - 1, 2):
                    if i + 1 >= len(expr) - 1:
                        return eval_expr(expr[i], new_scope)
                    val = eval_expr(expr[i + 1], new_scope)
                    new_scope[-1][expr[i]] = val
                return eval_expr(expr[-1], new_scope)

        tokens = tokenize(expression)
        parsed = parse(tokens)
        return eval_expr(parsed, [])
