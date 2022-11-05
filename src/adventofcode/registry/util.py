def get_registry_key(year: int, day: int, part: int, version: str = "normal") -> str:
    """Generate a key from the provided solution info"""
    if version:
        return f"{year}:{day}:{part}:{version}"

    return f"{year}:{day}:{part}:normal"


def get_info_from_registry_key(key: str) -> tuple[int, int, int, str]:
    """Decode registry key into solution info"""
    if len(segments := key.split(":")) == 0 or len(segments) < 4:
        raise ValueError("did not receive a valid registry key")

    year, day, part, version = segments
    return int(year), int(day), int(part), version
