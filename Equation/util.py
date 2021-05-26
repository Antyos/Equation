# -*- coding: utf-8 -*-
# ==============================================================================
#   Copyright 2014 AlphaOmega Technology
#
#   Licensed under the AlphaOmega Technology Open License Version 1.0
#   You may not use this file except in compliance with this License.
#   You may obtain a copy of the License at
#
#       http://www.alphaomega-technology.com.au/license/AOT-OL/1.0
# ==============================================================================


from typing import Callable, Union
# 'Literal' is not part of typing in py3.7
# See: https://github.com/python/typing/issues/707
try:
    from typing import Literal # type: ignore
except ImportError:
    from typing_extensions import Literal # type: ignore


try:
    from Equation import core
except ImportError:
    from . import core


def addFn(id: str, string: str, latex: str, num_args: Union[int, Literal["+"]], func: Callable):
    core.functions[id] = {"str": string, "latex": latex, "args": num_args, "func": func}


def addOp(id: str, str: str, latex: str, single: bool, prec: int, func: Callable):
    if single:
        raise RuntimeError("Single Ops Not Yet Supported")
    core.ops[id] = {"str": str, "latex": latex, "args": 2, "prec": prec, "func": func}


def addUnaryOp(id: str, string: str, latex: str, func: Callable):
    core.unary_ops[id] = {
        "str": string,
        "latex": latex,
        "args": 1,
        "prec": 0,
        "func": func,
    }


def addConst(name: str, value: Union[int, float, str]):
    core.constants[name] = value
