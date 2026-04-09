from circles_tattoo import CiclesDrawer, Circle

def main() -> None:
    circles = [
        Circle(line_width=5, num_terms=0, wobble_strength=0),
        Circle(line_width=2, num_terms=6, wobble_strength=2.5),
        Circle(line_width=2, num_terms=8, wobble_strength=3.0),
        Circle(line_width=2, num_terms=10, wobble_strength=2),
    ]

    drawer = CiclesDrawer(circles, seed=42)
    drawer.plot_circles(image_name="wobble_circles", show=True)

if __name__ == "__main__":
    main()