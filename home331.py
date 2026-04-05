from figures import (
    Triangle, Rectangle, Trapeze, Parallelogram, Circle,
    Ball, TriangularPyramid, QuadrangularPyramid,
    RectangularParallelepiped, Cone, TriangularPrism
)

FIGURE_MAP = {
    'Triangle':                 lambda p: Triangle(*p),
    'Rectangle':                lambda p: Rectangle(*p),
    'Trapeze':                  lambda p: Trapeze(*p),
    'Parallelogram':            lambda p: Parallelogram(*p),
    'Circle':                   lambda p: Circle(*p),
    'Ball':                     lambda p: Ball(*p),
    'TriangularPyramid':        lambda p: TriangularPyramid(*p),
    'QuadrangularPyramid':      lambda p: QuadrangularPyramid(*p),
    'RectangularParallelepiped':lambda p: RectangularParallelepiped(*p),
    'Cone':                     lambda p: Cone(*p),
    'TriangularPrism':          lambda p: TriangularPrism(*p),
}


def parse_line(line: str):
    """Parse one line from input file. Returns Figure or None on error."""
    line = line.strip()
    if not line:
        return None
    parts = line.split()
    name = parts[0]
    try:
        params = list(map(float, parts[1:]))
    except ValueError:
        return None

    if name not in FIGURE_MAP:
        return None

    try:
        figure = FIGURE_MAP[name](params)
        vol = figure.volume()
        if vol is None or vol < 0:
            return None
        return figure
    except Exception:
        return None


def load_figures(filepath: str) -> list:
    """Load all valid figures from a file."""
    figures = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            fig = parse_line(line)
            if fig is not None:
                figures.append(fig)
    return figures


def find_max_volume(figures: list):
    """Return figure with maximum volume()."""
    if not figures:
        return None
    return max(figures, key=lambda f: f.volume())


def process_file(filepath: str):
    print(f"\n{'='*50}")
    print(f"File: {filepath}")
    print(f"{'='*50}")

    figures = load_figures(filepath)
    print(f"Loaded {len(figures)} valid figures.")

    best = find_max_volume(figures)
    if best:
        print(f"Figure with max volume : {best.__class__.__name__}")
        print(f"Volume                 : {best.volume():.6f}")
        print(f"Dimension              : {best.dimension()}D")
        if best.dimension() == 2:
            print(f"Perimeter              : {best.perimeter():.6f}")
            print(f"Area                   : {best.square():.6f}")
        else:
            if best.squareBase() is not None:
                print(f"Base area              : {best.squareBase():.6f}")
            if best.squareSurface() is not None:
                print(f"Lateral surface area   : {best.squareSurface():.6f}")
            if best.height() is not None:
                print(f"Height                 : {best.height():.6f}")
    else:
        print("No valid figures found.")


if __name__ == '__main__':
    import sys
    import os

    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        # default: try all three input files
        files = ['input01.txt', 'input02.txt', 'input03.txt']

    for filepath in files:
        if os.path.exists(filepath):
            process_file(filepath)
        else:
            print(f"File not found: {filepath}")