from dataclasses import dataclass

@dataclass
class AppColors:
    isDarkMood: bool

    mainColor: str = "#580BD5"  # Base purple color

    # Colors for dark and light modes
    color0: tuple[str, str] = ("#000", "#fff")  # Light, Dark
    color1: tuple[str, str] = ("#650CF3", "#3C0792")  # Light, Dark
    color2: tuple[str, str] = ("#9355F6", "#320679")  # Light, Dark
    color3: tuple[str, str] = ("#A26DF8", "#280561")  # Light, Dark
    color4: tuple[str, str] = ("#C19EFA", "#1E0449")  # Light, Dark
    color5: tuple[str, str] = ("#E0CEFD", "#140231")  # Light, Dark

    # def __post_init__(self):
    #     self.mood(True)

    # def mood(self , isDarkMood:bool):
    #     self.isDarkMood = isDarkMood
    #     if self.isDarkMood:
    #         self.color1 = "#3C0792"  # Dark shade
    #         self.color2 = "#320679"  # Darker
    #         self.color3 = "#280561"  # Even darker
    #         self.color4 = "#1E0449"  # Close to black
    #         self.color5 = "#140231"  # Darkest
    #     else:
    #         self.color1 = "#650CF3"  # Light shade
    #         self.color2 = "#9355F6"  # Lighter
    #         self.color3 = "#A26DF8"  # Even lighter
    #         self.color4 = "#C19EFA"  # Close to white
    #         self.color5 = "#E0CEFD"  # Lightest

appColors = AppColors(isDarkMood=True)

# Example usage:
if(__name__ =="__main__"):
    dark_theme_colors = AppColors(isDarkMood=True)
    light_theme_colors = AppColors(isDarkMood=False)

    print("Dark theme colors:", dark_theme_colors)
    print("Light theme colors:", light_theme_colors)
