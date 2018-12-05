import re

claim_re = re.compile('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')

with open('input/day3_input') as i:
    with open('input/day3_input.lp', 'w+') as o:
        for line in i:
            claim = claim_re.match(line.strip())
            o.write('claim({}, {}, {}, {}, {}).\n'.format(claim[1], claim[2], claim[3], claim[4], claim[5]))
