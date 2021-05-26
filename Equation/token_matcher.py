import re
from typing import Callable, Literal, Union

from Equation import util

global constants
global unary_ops
global ops
global functions
global smatch
global vmatch
global nmatch
global gsmatch
global gematch
global fmatch
global omatch
global umatch

constants: dict = {}
unary_ops: dict = {}
ops: dict = {}
functions: dict = {}

smatch = re.compile(r"\s*,") # Separator

# Values
# fmt: off
vmatch = re.compile(
    r"\s*"
    r"(?:"
        r"(?P<oct>"
            r"(?P<octsign>[+-]?)"
            r"\s*0o"
            r"(?P<octvalue>[0-7]+)"
        r")|(?P<hex>"
            r"(?P<hexsign>[+-]?)"
            r"\s*0x"
            r"(?P<hexvalue>[0-9a-fA-F]+)"
        r")|(?P<bin>"
            r"(?P<binsign>[+-]?)"
            r"\s*0b"
            r"(?P<binvalue>[01]+)"
        r")|(?P<dec>"
            r"(?P<rsign>[+-]?)"
            r"\s*"
            r"(?P<rvalue>(?:\d+\.\d+|\d+\.|\.\d+|\d+))"
            r"(?:"
                r"[Ee]"
                r"(?P<rexpoent>[+-]?\d+)"
            r")?"
            r"(?:"
                r"\s*"
                r"(?P<sep>(?(rvalue)\+|))?"
                r"\s*"
                r"(?P<isign>(?(rvalue)(?(sep)[+-]?|[+-])|[+-]?)?)"
                r"\s*"
                r"(?P<ivalue>(?:\d+\.\d+|\d+\.|\.\d+|\d+))"
                r"(?:"
                    r"[Ee]"
                    r"(?P<iexpoent>[+-]?\d+)"
                r")?"
                r"[ij]"
            r")?"
        r")"
    r")"
)
# fmt: on

nmatch = re.compile(r"\s*([a-zA-Z_][a-zA-Z0-9_]*)") # Name
gsmatch = re.compile(r"\s*(\()") # Group start
gematch = re.compile(r"\s*(\))") # Group end


def recalculateFMatch():
    global fmatch, omatch, umatch
    fks = sorted(functions.keys(), key=len, reverse=True)
    oks = sorted(ops.keys(), key=len, reverse=True)
    uks = sorted(unary_ops.keys(), key=len, reverse=True)
    fmatch = re.compile(r"\s*(" + r"|".join(map(re.escape, fks)) + r")")
    omatch = re.compile(r"\s*(" + r"|".join(map(re.escape, oks)) + r")")
    umatch = re.compile(r"\s*(" + r"|".join(map(re.escape, uks)) + r")")


def addFn(id: str, string: str, latex: str, num_args: Union[int, Literal["+"]], func: Callable):
    _id, _fn = util.addFn(id, string, latex, num_args, func)
    functions[_id] = _fn


def addOp(id: str, string: str, latex: str, single: bool, prec: int, func: Callable):
    if single:
        raise RuntimeError("Single Ops Not Yet Supported")
    _id, _op = util.addOp(id, string, latex, single, prec, func)
    ops[_id] = _op


def addUnaryOp(id: str, string: str, latex: str, func: Callable):
    _id, _uop = util.addUnaryOp(id, string, latex, func)
    unary_ops[_id] = _uop


def addConst(name: str, value: Union[int, float, str]):
    _name, _value = util.addConst(name, value)
    constants[_name] = _value
