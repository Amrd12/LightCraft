from dataclasses import dataclass
@dataclass
class AppColors:
    isDarkMood: bool

    mainColor: str = "#580BD5"  # Base purple color

    # Colors for dark and light modes
    color1: str = None
    color2: str = None
    color3: str = None
    color4: str = None
    color5: str = None

    def __post_init__(self):
        if self.isDarkMood:
            self.color1 = "#3C0792"  # Dark shade
            self.color2 = "#320679"  # Darker
            self.color3 = "#2A055E"  # Even darker
            self.color4 = "#21044A"  # Close to black
            self.color5 = "#190337"  # Darkest
        else:
            self.color1 = "#650CF3"  # Light shade
            self.color2 = "#9355F3"  # Lighter
            self.color3 = "#B17EF5"  # Even lighter
            self.color4 = "#CFA7F7"  # Close to white
            self.color5 = "#E0C7F8"  # Lightest

# Example usage:
if(__name__ =="__main__"):
    dark_theme_colors = AppColors(isDarkMood=True)
    light_theme_colors = AppColors(isDarkMood=False)

    print("Dark theme colors:", dark_theme_colors)
    print("Light theme colors:", light_theme_colors)
