import numpy as np
import matplotlib.pyplot as plt
from numpy.random import Generator

class Circle:
    """Represents a wobbling circle with configurable drawing parameters.

    Parameters
    ----------
    radius
        Base radius of the circle.
    origin
        Center position of the circle as (x, y).
    line_width
        Width of the circle outline.
    num_terms
        Number of Fourier terms used to generate the wobble..
    wobble_strength
        Maximum radial deformation applied to the circle
    """
    def __init__(
        self,
        radius: float = 10.0,
        origin: tuple[float, float] = (0.0, 0.0),
        line_width: float = 2.0,
        num_terms: int = 5,
        wobble_strength: float = 0.5
    ) -> None:
        self.radius = radius
        self.origin = origin
        self.line_width = line_width
        self.num_terms = num_terms
        self.wobble_strength = float(wobble_strength)


class CiclesDrawer:
    """Wrapper class used to draw the final image.

    Parameters
    ----------
    circles
        List of circles instances to be drawn together.
    rng
        Random seed.
    """
    def __init__(self, circles: list[Circle], seed: int = 42) -> None:
        self.circles = circles
        self.rng: Generator = np.random.default_rng(seed)

    def _draw_smooth_wobble_circle(
        self,
        circle: Circle,
        resolution: int = 600
    ) -> None:
        """Draw a smooth wobbling circle using a Fourier-based radial deformation.

        Parameters
        ----------
        circle
            Circle instance to be drawn. 
        resolution
            Number of points used to draw the circle.
        """
        theta = np.linspace(0, 2 * np.pi, resolution)
        offsets = np.zeros_like(theta)

        for n in range(1, max(1, circle.num_terms) + 1):
            a = self.rng.uniform(-1, 1)
            b = self.rng.uniform(-1, 1)
            offsets += (a * np.sin(n * theta) + b * np.cos(n * theta)) / n

        max_offset = float(np.max(np.abs(offsets)))
        if max_offset > 0:
            offsets = offsets / max_offset * circle.wobble_strength

        r = circle.radius + offsets
        x = circle.origin[0] + r * np.cos(theta)
        y = circle.origin[1] + r * np.sin(theta)

        plt.plot(x, y, color='black', linewidth=circle.line_width)

    def plot_circles(self, image_name: str | None = None, show: bool = True) -> None:
        """Draw circles plot.

        Parameters
        ----------
        image_name
            Output image name.
        show
            Boolean flag to show plot before saving it. 
        """
        plt.figure(facecolor='white')

        for circle in self.circles:
            self._draw_smooth_wobble_circle(circle)

        ax = plt.gca()
        ax.set_aspect('equal')
        ax.axis('off')

        if image_name:
            if not image_name.endswith(".png"):
                image_name += ".png"
            plt.savefig(image_name, dpi=300, bbox_inches='tight', pad_inches=0)

        if show:
            plt.show()
        else:
            plt.close()