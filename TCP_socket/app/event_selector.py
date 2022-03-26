import selectors


def set_selector_events_mask(mode: str) -> int:
    """Set selector to listen for events: mode is 'r', 'w', or 'rw'."""

    if mode not in {'r', 'w', 'rw'}:
        raise ValueError(f"Invalid events mask mode {mode!r}.")

    return {"r": selectors.EVENT_READ,
            "w": selectors.EVENT_WRITE,
            "rw": selectors.EVENT_READ | selectors.EVENT_WRITE}[mode]

