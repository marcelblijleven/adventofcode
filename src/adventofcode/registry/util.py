NO_VALID_REGISTRY_KEY = "did not receive a valid registry key"


def get_registry_key(year: int, day: int, part: int, version: str = "normal") -> str:
    """Generate a key from the provided solution info"""
    if version:
        return f"{year}:{day}:{part}:{version}"

    return f"{year}:{day}:{part}:normal"


def get_info_from_registry_key(key: str) -> tuple[int, int, int, str]:
    """Decode registry key into solution info"""
    min_bound = 0
    max_bound = 4

    if len(segments := key.split(":")) == min_bound or len(segments) < max_bound:
        raise ValueError(NO_VALID_REGISTRY_KEY)

    year, day, part, version = segments
    return int(year), int(day), int(part), version
