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
        self.mood(True)

    def mood(self , isDarkMood:bool):
        self.isDarkMood = isDarkMood
        if self.isDarkMood:
            self.color1 = "#3C0792"  # Dark shade
            self.color2 = "#320679"  # Darker
            self.color3 = "#280561"  # Even darker
            self.color4 = "#1E0449"  # Close to black
            self.color5 = "#140231"  # Darkest
        else:
            self.color1 = "#650CF3"  # Light shade
            self.color2 = "#9355F6"  # Lighter
            self.color3 = "#A26DF8"  # Even lighter
            self.color4 = "#C19EFA"  # Close to white
            self.color5 = "#E0CEFD"  # Lightest

appColors = AppColors(isDarkMood=True)

# Example usage:
if(__name__ =="__main__"):
    dark_theme_colors = AppColors(isDarkMood=True)
    light_theme_colors = AppColors(isDarkMood=False)

    print("Dark theme colors:", dark_theme_colors)
    print("Light theme colors:", light_theme_colors)
