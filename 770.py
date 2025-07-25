from typing import List
import re
from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        # map known variables to their integer values
        valmap = dict(zip(evalvars, evalints))

        # tokenize into numbers, vars, operators, parentheses
        tokens = re.findall(r'\w+|[+*\-()]', expression)

        # helper to create a term-dict from a single token
        def make_term(tok):
            if tok.isdigit():
                return {(): int(tok)}
            if tok in valmap:
                return {(): valmap[tok]}
            # symbolic variable
            return {(tok,): 1}

        # add two term‐dicts (allows negative results)
        def add_terms(A, B):
            R = A.copy()
            for k, v in B.items():
                R[k] = R.get(k, 0) + v
                if R[k] == 0:
                    del R[k]
            return R

        # subtract B from A
        def sub_terms(A, B):
            R = A.copy()
            for k, v in B.items():
                R[k] = R.get(k, 0) - v
                if R[k] == 0:
                    del R[k]
            return R

        # multiply two term‐dicts
        def mul_terms(A, B):
            R = {}
            for k1, v1 in A.items():
                for k2, v2 in B.items():
                    key = tuple(sorted(k1 + k2))
                    R[key] = R.get(key, 0) + v1 * v2
            # drop zeros
            return {k: v for k, v in R.items() if v != 0}

        # recursive descent parser with proper precedence
        def parse_expression(idx=0):
            terms, idx = parse_term(idx)
            while idx < len(tokens) and tokens[idx] in ('+', '-'):
                op = tokens[idx]; idx += 1
                right, idx = parse_term(idx)
                terms = add_terms(terms, right) if op == '+' else sub_terms(terms, right)
            return terms, idx

        def parse_term(idx):
            factors, idx = parse_factor(idx)
            while idx < len(tokens) and tokens[idx] == '*':
                idx += 1
                right, idx = parse_factor(idx)
                factors = mul_terms(factors, right)
            return factors, idx

        def parse_factor(idx):
            tok = tokens[idx]
            if tok == '(':
                idx += 1
                expr_terms, idx = parse_expression(idx)
                idx += 1  # skip ')'
                return expr_terms, idx
            else:
                return make_term(tok), idx + 1

        # kick off parsing
        final_terms, _ = parse_expression(0)

        # format and sort: degree desc, lex order
        def fmt(key, coeff):
            if key:
                return f"{coeff}*" + "*".join(key)
            else:
                return str(coeff)

        result = []
        for key in sorted(final_terms.keys(), key=lambda k: (-len(k), k)):
            coeff = final_terms[key]
            if coeff != 0:
                result.append(fmt(key, coeff))
        return result
