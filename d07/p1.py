from __future__ import annotations

dirs = {}

class Dir:
    def __init__(self, name: str, parent: Dir | None = None):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files_size = 0

    def __repr__(self):
        return f'<{self.name}: {self.size} [dirs: {self.dirs}]>'

    @property
    def size(self):
        return sum(x.size for x in self.dirs.values()) + self.files_size

    @property
    def full_path(self):
        p = []
        cur = self.parent
        while cur:
            p.append(cur.name)
            cur = cur.parent
        return ':'.join(reversed(p)) + ':' + self.name


def calc_size(d: Dir, lim: int):
    s = 0
    for chd in d.dirs.values():
        s += calc_size(chd, lim)
    s += d.files_size
    if s <= lim:
        dirs[d.full_path] = s
    return s


def run(inp):
    root = Dir('/')
    cur = root
    for line in inp:
        p = line.split(' ')
        if p[0] == '$':
            if p[1] == 'cd':
                dirname = p[2]
                if dirname == '/':
                    continue
                if dirname == '..':
                    cur = cur.parent
                    continue
                cur = cur.dirs[dirname]
            else:  # ls
                continue
        elif p[0] == 'dir':
            cur.dirs[p[1]] = Dir(p[1], cur)
            continue
        else:
            cur.files_size += int(p[0])

    calc_size(root, 100000)
    return sum(dirs.values())