seeds_input = open('input51.txt', 'r').readlines()

def parse_input(s):
    groups = s.split('\n\n')

    seeds = list(map(int, groups[0].split()[1:]))

    maps = {}
    for mapping in groups[1:]:
        lines = mapping.splitlines()
        key = lines[0].split()[0]
        a, b = key.split('-to-')
        maps[a, b] = [tuple(map(int, l.split())) for l in lines[1:]]

    return seeds, maps

seeds, mappings = parse_input("".join(seeds_input))

def find_sequence(maps, start_type, end_type):
    seq = [start_type]

    while start_type != end_type:
        start_type = next(b for a, b in maps if a == start_type)
        seq.append(start_type)

    return seq

def do_mapping(val, maps, seq):
    for a, b in zip(seq, seq[1:]):
        mapping = maps[a, b]

        if any(mapping):
            for dst, src, size in mapping:
                if src <= val < src + size:
                    val = dst + (val - src)
                    break

    return val

def calculate_min_distance(seeds, maps):
    seq = find_sequence(maps, 'seed', 'location')
    return min(do_mapping(val, maps, seq) for val in seeds)

# Print the result
result = calculate_min_distance(seeds, mappings)
print("Location number:", result)
