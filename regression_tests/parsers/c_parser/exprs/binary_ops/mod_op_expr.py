"""
    A modulo operator (``%``).
"""

from regression_tests.parsers.c_parser.exprs.binary_ops.binary_op_expr import BinaryOpExpr


class ModOpExpr(BinaryOpExpr):
    """A modulo operator (``%``)."""

    def is_mod_op(self):
        """Returns ``True``."""
        return True

    def __str__(self):
        return '{} % {}'.format(self.lhs, self.rhs)
