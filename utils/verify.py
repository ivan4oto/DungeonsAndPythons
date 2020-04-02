from collections import Iterable


def verify_types(*args, **kwargs):
    expected_types = kwargs

    def decorator(func):
        def type_check(self, *args, **kwargs):
            arguments = list(args)
            result = {}
            for argument, type_of_arg in zip(arguments, expected_types.values()):
                result[argument] = type_of_arg

            for key, value in result.items():
                if not isinstance(key, value):
                    raise TypeError(
                        f'TypeError: Argument {key} of {func} is not {value}!')
            return func(self, *args, **kwargs)

        return type_check

    return decorator


def verify_positive(func):
    def check_positive(self, *args, **kwargs):
        for arg in args:
            if (type(arg) is float or type(arg) is int) and arg < 0:
                raise ValueError("ValueError: Positive number requested!")
        for arg in kwargs:
            if (type(arg) is float or type(arg) is int) and arg < 0:
                raise ValueError("ValueError: Positive number requested!")
        return func(self, *args, **kwargs)

    return check_positive
