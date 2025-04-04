from typing import ClassVar, Union

# adapted from: https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb


class PrecisionRangeError(Exception):
    def __init__(self, number):
        super().__init__(f"precision must be an int (range 0-3), but given value {number} does not fall in this range.")


class HumanBytes:
    METRIC_LABELS: ClassVar[list[str]] = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    BINARY_LABELS: ClassVar[list[str]] = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
    PRECISION_OFFSETS: ClassVar[list[float]] = [0.5, 0.05, 0.005, 0.0005]  # PREDEFINED FOR SPEED.
    PRECISION_FORMATS: ClassVar[list[str]] = [
        "{}{:.0f} {}",
        "{}{:.1f} {}",
        "{}{:.2f} {}",
        "{}{:.3f} {}",
    ]  # PREDEFINED FOR SPEED.

    @staticmethod
    def format(num: Union[int, float], metric: bool = False, precision: int = 1) -> str:
        """
        Human-readable formatting of bytes, using binary (powers of 1024)
        or metric (powers of 1000) representation.
        """

        if precision < 0 and precision > 3:
            raise PrecisionRangeError(precision)

        unit_labels = HumanBytes.METRIC_LABELS if metric else HumanBytes.BINARY_LABELS
        last_label = unit_labels[-1]
        unit_step = 1000 if metric else 1024
        unit_step_thresh = unit_step - HumanBytes.PRECISION_OFFSETS[precision]

        is_negative = num < 0
        if is_negative:  # Faster than ternary assignment or always running abs().
            num = abs(num)

        for unit in unit_labels:
            if num < unit_step_thresh:
                # VERY IMPORTANT:
                # Only accepts the CURRENT unit if we're BELOW the threshold where
                # float rounding behavior would place us into the NEXT unit: F.ex.
                # when rounding a float to 1 decimal, any number ">= 1023.95" will
                # be rounded to "1024.0". Obviously we don't want ugly output such
                # as "1024.0 KiB", since the proper term for that is "1.0 MiB".
                break
            if unit != last_label:
                # We only shrink the number if we HAVEN'T reached the last unit.
                # NOTE: These looped divisions accumulate floating point rounding
                # errors, but each new division pushes the rounding errors further
                # and further down in the decimals, so it doesn't matter at all.
                num /= unit_step

        return HumanBytes.PRECISION_FORMATS[precision].format("-" if is_negative else "", num, unit)


# print(HumanBytes.format(2251799813685247)) # 2 pebibytes
# print(HumanBytes.format(2000000000000000, True)) # 2 petabytes
# print(HumanBytes.format(1099511627776)) # 1 tebibyte
# print(HumanBytes.format(1000000000000, True)) # 1 terabyte
# print(HumanBytes.format(1000000000, True)) # 1 gigabyte
# print(HumanBytes.format(4318498233, precision=3)) # 4.022 gibibytes
# print(HumanBytes.format(4318498233, True, 3)) # 4.318 gigabytes
# print(HumanBytes.format(-4318498233, precision=2)) # -4.02 gibibytes
