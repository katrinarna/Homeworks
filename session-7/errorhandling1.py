import argparse

def set_theme(theme="default"):
    valid_themes = ["default", "light", "dark", "blue"]
    if theme not in valid_themes:
        raise ValueError(f"Invalid theme: {theme}")
    print(f"Theme set to {theme}")

parser = argparse.ArgumentParser(description="Set the application theme")

parser.add_argument(
    "--theme",
    default="default",
    help="Theme to set. Valid options: default, light, dark, blue"
)

args = parser.parse_args()

try:
    set_theme(args.theme)
except ValueError as e:
    print(f"Oops! {e}")
    print("Falling back to default theme...")
    set_theme()  
