code_to_color = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
                 "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887",
                 "cadetblue": "#5f9ea0", "chocolate": "#d2691e", }
color_name = input("Enter color name: ").lower()
while color_name != "":
    if color_name in code_to_color:
        print(color_name, "is", code_to_color[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()