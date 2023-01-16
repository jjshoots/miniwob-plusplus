"""Gymnasium environment registration."""
from gymnasium.envs.registration import register

MINIWOB_TASKS = [
    "bisect-angle",
    "book-flight",
    "book-flight-nodelay",
    # "chase-circle",   # Depends on the clock
    "choose-date",
    "choose-date-easy",
    "choose-date-medium",
    "choose-date-nodelay",
    "choose-list",
    "circle-center",
    "click-button",
    "click-button-sequence",
    "click-checkboxes",
    "click-checkboxes-large",
    "click-checkboxes-soft",
    "click-checkboxes-transfer",
    "click-collapsible",
    "click-collapsible-2",
    "click-collapsible-2-nodelay",
    "click-collapsible-nodelay",
    "click-color",
    "click-dialog",
    "click-dialog-2",
    "click-link",
    "click-menu",
    "click-menu-2",
    "click-option",
    "click-pie",
    "click-pie-nodelay",
    "click-scroll-list",
    "click-shades",
    "click-shape",
    "click-tab",
    "click-tab-2",
    "click-tab-2-easy",
    "click-tab-2-hard",
    "click-tab-2-medium",
    "click-test",
    "click-test-2",
    "click-test-transfer",
    "click-widget",
    "copy-paste",
    "copy-paste-2",
    "count-shape",
    "count-sides",
    "drag-box",
    "drag-cube",
    "drag-item",
    "drag-items",
    "drag-items-grid",
    "drag-shapes",
    "drag-sort-numbers",
    "email-inbox",
    "email-inbox-delete",
    "email-inbox-forward",
    "email-inbox-forward-nl",
    "email-inbox-forward-nl-turk",
    "email-inbox-important",
    "email-inbox-nl-turk",
    "email-inbox-noscroll",
    "email-inbox-reply",
    "email-inbox-star-reply",
    "enter-date",
    "enter-password",
    "enter-text",
    "enter-text-2",
    "enter-text-dynamic",
    "enter-time",
    "find-midpoint",
    "find-word",
    "focus-text",
    "focus-text-2",
    "grid-coordinate",
    "guess-number",
    "highlight-text",
    "highlight-text-2",
    "identify-shape",
    "login-user",
    "login-user-popup",
    # "moving-items",   # Depends on the clock
    "multi-layouts",
    "multi-orderings",
    "navigate-tree",
    "number-checkboxes",
    "read-table",
    "read-table-2",
    "resize-textarea",
    "right-angle",
    "scroll-text",
    "scroll-text-2",
    "search-engine",
    "simon-says",
    "simple-algebra",
    "simple-arithmetic",
    "social-media",
    "social-media-all",
    "social-media-some",
    "terminal",
    "text-editor",
    "text-transform",
    "tic-tac-toe",
    # "unicode-test",   # Not in the canonical task set; contains Unicode
    "use-autocomplete",
    "use-autocomplete-nodelay",
    "use-colorwheel",
    "use-colorwheel-2",
    "use-slider",
    "use-slider-2",
    "use-spinner",
    "visual-addition",
]
FLIGHTWOB_TASKS = ["AA", "Alaska", "Alaska-auto", "Alaska-auto-medium"]

NON_DETERMINISTIC_TASKS = [
    "click-pie",
]


def register_miniwob_envs():
    """Register MiniWoB and FlightWoB environments."""
    for name in MINIWOB_TASKS:
        register(
            id=f"miniwob/{name}-v1",
            entry_point="miniwob.environment:MiniWoBEnvironment",
            kwargs={"subdomain": name},
            nondeterministic=(name in NON_DETERMINISTIC_TASKS),
        )
    for name in FLIGHTWOB_TASKS:
        register(
            id=f"miniwob/flight.{name}-v1",
            entry_point="miniwob.environment:MiniWoBEnvironment",
            kwargs={"subdomain": f"flight.{name}"},
        )
