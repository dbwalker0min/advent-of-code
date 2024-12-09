from copy import copy
from typing import IO
from dataclasses import dataclass
import tqdm

def read_disk_map(fid: IO[str]) -> list[int]:
    """Read a compressed disk map and converted to a sector map"""
    line = fid.readline()
    if not line:
        raise ValueError("Empty file")

    # get rid of line terminator
    line = line.rstrip()

    sector_map = []
    id = 0
    while line:
        cnt, line = line[0], line[1:]
        check_compressed_char(cnt)
        sector_map.extend([id] * int(cnt))
        id += 1
        if line:
            free, line = line[0], line[1:]
            check_compressed_char(free)
            sector_map.extend([-1]*int(free))

    return sector_map


def print_map_for_debug(sector_map):
    print('map')
    print(''.join(str(s) if s >= 0 else '.' for s in sector_map))


def compute_checksum(sector_map: list[int]):
    """Compute the checksum of the sector map"""
    return sum([id*pos for pos, id in enumerate(sector_map) if id >= 0])

def check_compressed_char(cnt):
    """Make certain the compressed character is in the proper range"""
    if not ('0' <= cnt <= '9'):
        raise ValueError(f'Invalid character "{cnt}"')

def defragment(fid: IO[str]) -> int:
    """Defragment the disk given the compressed disk map"""

    disk_map = read_disk_map(fid)
    disk_map_reversed = disk_map[::-1]

    while 1:
        try:
            first = next(i for i, x in enumerate(disk_map) if x < 0)
            end = len(disk_map) - next(i for i, x in enumerate(disk_map_reversed) if x >= 0) - 1
            if first > end:
                break
            disk_map[first] = disk_map[end]
            disk_map[end] = -1
            disk_map_reversed[len(disk_map) - 1 - first] = disk_map[first]
            disk_map_reversed[len(disk_map) - 1 - end] = -1
        except StopIteration:
            break
    return compute_checksum(disk_map)

def find_first_gap(map: list[int], min_size: int):

    pass

@dataclass(frozen=True)
class DiskSegment():
    length : int = None
    id: int = None

def move_seg(segs: list[DiskSegment], seg: DiskSegment) -> None:
    for seg_num, s in enumerate(segs):
        # don't go past this segment. I know all the segments are unique.
        if s == seg:
            return

        if s.id == -1 and s.length >= seg.length:
            # this segment is big enough.
            # Move it

            # the index of the element of `seg` needs to be set to free
            seg_index = next(i for i, s in enumerate(segs) if s == seg)

            # Make the target segment free. If a free block precedes or follows it, then that segment will be extended
            updated = False
            for diff in [-1, 1]:
                try:
                    if segs[seg_index + diff].id == -1:
                        # The preceding or next segment is free. Extend it.
                        segs[seg_index + diff] = DiskSegment(id=-1, length=segs[seg_index + diff].length + seg.length)
                        segs.remove(seg)
                        updated = True
                        break
                except IndexError:
                    pass
            if not updated:
                segs[seg_index] = DiskSegment(id=-1, length=seg.length)

            # Move the segment to the free space. It may be necessary to add a free segment.
            # I know that a free segment cannot precede or follow this segment
            old_free_seg_len = segs[seg_num].length
            segs[seg_num] = seg

            # Do I need to insert a free segment here
            if seg.length < old_free_seg_len:
                free_seg = DiskSegment(id=-1, length=old_free_seg_len - seg.length)
                segs.insert(seg_num + 1, free_seg)

            return

def defragment2(fid: IO[str]) -> int:
    disk_map = read_disk_map(fid)

    # convert disk map to disk segments
    segments: list[DiskSegment]= []
    length = None
    segment_id = None
    for seg_id in disk_map:
        if seg_id != segment_id:
            if segment_id is not None:
                segments.append(DiskSegment(id=segment_id, length=length))
            segment_id = seg_id
            length = 1
        else:
            # increase its length
            length += 1
    # At the end, save the incomplete segment
    segments.append(DiskSegment(id=segment_id, length=length))

    # go from the highest ID to the smallest and attempt to move down
    segment_ids = [s for s in segments[::-1] if s.id >= 0]
    with tqdm.tqdm(total=len(segment_ids)) as pbar:
        for seg_to_move in segment_ids:
            s: DiskSegment = copy(seg_to_move)
            move_seg(segments, s)
            pbar.update()

    # expand the segments back to the map
    map = []
    for s in segments:
        map.extend([s.id]*s.length)

    return compute_checksum(map)



