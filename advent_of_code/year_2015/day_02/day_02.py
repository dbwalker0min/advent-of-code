from io import TextIOBase
import dataclasses

@dataclasses.dataclass
class Result:
    paper_area: int = 0
    bow_length: int = 0

    def __add__(self, b: 'Result'):
        return Result(self.paper_area + b.paper_area, self.bow_length + b.bow_length)

def compute_area(package_size: str) -> Result:
    """Compute the amount of wrapping paper to wrap the package."""

    # An empty line has no package size
    if not package_size:
        return 0

    len, width, depth = [int(s) for s in package_size.split('x')]

    # compute the areas of each face
    areas = [len*width, len*depth, width*depth]
    bow_length = 2*min([len + width, len + depth, width+depth]) + len*width*depth

    paper_area = 2*sum(areas) + min(areas)

    return Result(paper_area, bow_length)

def compute_area_file(f: TextIOBase) -> Result:
    """Compute the total area for all packages in file"""

    result = Result()
    for line in f:
        result += compute_area(line.strip())

    return result
