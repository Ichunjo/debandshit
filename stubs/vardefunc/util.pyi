import vapoursynth as vs
from typing import Any, Callable, List, Sequence, Tuple, Union

core: Any

class FormatError(Exception): ...

def copy_docstring_from(source: Callable[..., Any]) -> Callable[..., Any]: ...
def get_sample_type(clip: vs.VideoNode) -> vs.SampleType: ...
def load_operators_expr() -> List[str]: ...
def mae_expr(gray_only: bool=...) -> str: ...
def max_expr(n: int) -> str: ...
def pick_px_op(use_expr: bool, operations: Tuple[str, Union[Sequence[int], Sequence[float], int, float, Callable[..., Any]]]) -> Any: ...
def rmse_expr(gray_only: bool=...) -> str: ...