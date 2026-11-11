"""One simple, safe tool for the Day 1 agent: a calculator.

The tool parses a plain arithmetic phrase like "19 plus 23" or "7 * 6"
using the Python ast module with a strict allowlist. No eval, no imports.
"""
import ast
import operator

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}

_WORDS = {"plus": "+", "minus": "-", "times": "*", "multiplied by": "*",
          "divided by": "/", "over": "/"}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.operand))
    raise ValueError("Unsupported expression")


def calculator(expression: str) -> float:
    """Evaluate a simple arithmetic expression and return the number."""
    text = expression.strip().lower()
    for word, symbol in sorted(_WORDS.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(word, symbol)
    # Keep only digits, operators, dots, spaces and parentheses
    allowed = set("0123456789+-*/.() ")
    text = "".join(ch for ch in text if ch in allowed).strip()
    if not text:
        raise ValueError("No arithmetic expression found")
    return _eval(ast.parse(text, mode="eval"))
