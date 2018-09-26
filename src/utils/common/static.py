
import os
import sys

__exec_dir = sys.path[0]
while os.path.basename(__exec_dir) != "src":
	__exec_dir = os.path.dirname(__exec_dir)
	sys.path.insert(0, __exec_dir)


def static_vars(**kwargs):
    """Create a decorator for using static variables.

	Arguments:
		kwargs: Dictionary containing initial values of static variables.
	"""
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate
