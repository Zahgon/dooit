class DooitThemeBase:
    _name: str = "dooit-base"

    # background colors
    background1: str = "#2E3440"  # Darkest
    background2: str = "#3B4252"  # Lighter
    background3: str = "#434C5E"  # Lightest

    # foreground colors
    foreground1: str = "#D8DEE9"  # Darkest
    foreground2: str = "#E5E9F0"  # Lighter
    foreground3: str = "#ECEFF4"  # Lightest

    # other colors
    red: str = "#BF616A"
    orange: str = "#D08770"
    yellow: str = "#EBCB8B"
    green: str = "#A3BE8C"
    blue: str = "#81A1C1"
    purple: str = "#B48EAD"
    magenta: str = "#B48EAD"
    cyan: str = "#8FBCBB"

    # accent colors
    primary: str = cyan
    secondary: str = blue

    @classmethod
    def to_css(cls) -> str:
        pass
