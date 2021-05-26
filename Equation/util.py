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


from typing import Callable, Literal, Union


try:
    from Equation import core
except ImportError:
    from . import core


def addFn(
    id: str, string: str, latex: str, num_args: Union[int, Literal["+"]], func: Callable
):
    return (id, {"str": string, "latex": latex, "args": num_args, "func": func})


def addOp(id: str, string: str, latex: str, single: bool, prec: int, func: Callable):
    if single:
        raise RuntimeError("Single Ops Not Yet Supported")
    return (id, {"str": string, "latex": latex, "args": 2, "prec": prec, "func": func})


def addUnaryOp(id: str, string: str, latex: str, func: Callable):
    return (id, {"str": string, "latex": latex, "args": 1, "prec": 0, "func": func})


def addConst(name: str, value: Union[int, float, str]):
    return (name, value)
