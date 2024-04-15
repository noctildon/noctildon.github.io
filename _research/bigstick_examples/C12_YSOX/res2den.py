"""
Convert BIGSTICK .dres to .dat to the inputs to mathematica

Steps
1. Rmove the heading and ending in nuclues.dres
2. Add one blank line in the beginning
3. Change T, orbits, and the final state number
4. Move nucleus.dres to the folder with this file exists
5. python3 res2den.py
6. Clean the output .dat a bit
"""
from math import sqrt

# valence orbits: n, 2j, l, N
sdpf = [[0, 5, 2, 2], [1, 1, 0, 2], [0, 3, 2, 2],
        [0, 7, 3, 3], [1, 3, 1, 3], [0, 5, 3, 3], [1, 1, 1, 3]]

psd =  [[0, 1, 1, 1], [0, 3, 1, 1],
        [0, 5, 2, 2], [1, 1, 0, 2], [0, 3, 2, 2]]

jj55 = [[0, 7, 4, 4],[1, 5, 2, 4],[1, 3, 2, 4],[2, 1, 0, 4],[0, 11, 5, 5]]


# Set the operator isospin and orbits (.sps)
T = 1
orbits = psd

headline = 'ONE-BODY DENSITY MATRIX FOR 2JO = {} TO =, {}\n'
threshold = 1e-5
def dres2dat(input, output, isospin=True):
    out = ''
    with open(input) as f:
        lines = f.readlines()
        Jt = float(lines[2].split()[2][0])

        out += headline.format(int(Jt*2), 0)
        for n in range(3, len(lines)):
            line = lines[n].split()
            if 'Jt' in line:
                Jt_ = int(line[2][:-1])
                out += headline.format(int(Jt_*2), 0)
                continue

            orba, orbb, me0, me1 = line
            e = [orba, orbb, me0, me1]
            if abs(float(me0)) > threshold:
                out += genDenLine(e,0,isospin=isospin)

        out += headline.format(int(Jt*2), 2)
        for n in range(3, len(lines)):
            line = lines[n].split()
            if 'Jt' in line:
                Jt_ = int(line[2][:-1])
                out += headline.format(int(Jt_*2), 2)
                continue

            orba, orbb, me0, me1 = line
            e = [orba, orbb, me0, me1]
            if abs(float(me1)) > threshold:
                out += genDenLine(e,1,isospin=isospin)

    print(out)
    save(out, output)


def save(content, filename):
    with open(filename, 'w') as f:
        f.write(content)

def wT0(p, n, T=T):
    return (p + n) * sqrt(2*T+1) / sqrt(2)

def wT1(p, n, T=T):
    return (p - n) * sqrt(2*T+1) * sqrt(T*(T+1)) / T / sqrt(6)


def genDenLine(e, T0, isospin=True):
    n_index = 3 # N principal quantum number
    # n_index = 0 # n nodal/radial quantum number
    orbit_in = orbits[int(e[0]) - 1]
    orbit_out = orbits[int(e[1]) - 1]
    N_in = orbit_in[n_index]
    j_in = orbit_in[1]
    N_out = orbit_out[n_index]
    j_out = orbit_out[1]

    if isospin:
        # isospin format
        me0 = e[2]
        me1 = e[3]
    else:
        # pn format
        me0 = wT0(float(e[2]), float(e[3]))
        me1 = wT1(float(e[2]), float(e[3]))

    if T0 == 0:
        return '{} {} {} {}   {}\n'.format(N_in, j_in, N_out, j_out, me0)
    elif T0 == 1:
        return '{} {} {} {}   {}\n'.format(N_in, j_in, N_out, j_out, me1)


# extract n=i->j from .dres files
# ground state is n=1
def preprocess(input, output, statej=2, statei=1):
    matrix = ''
    starting_line, ending_line = 0, 0
    with open(input) as f:
        unsplit_lines = f.readlines()
        lines = []
        for line in unsplit_lines:
            line = line.split()
            if line and '++++' in line[0]:
                line = []
            lines.append(line)

        for i in range(len(lines)):
            if 'Initial' in lines[i] and 'state' in lines[i]:
                if statei == int(lines[i][3]) and statej == int(lines[i+1][3]):
                    starting_line = i

        while True:
            line_pivot = starting_line + ending_line
            if lines[line_pivot] == []:
                break
            ending_line += 1
        ending_line = starting_line + ending_line

        for l in range(starting_line, ending_line):
            matrix += unsplit_lines[l]
    # print(matrix)
    save(matrix, output)


def main(nucleus, statej):
    statei = 1

    file1 = nucleus + '.dres'
    file2 = nucleus + '_obdm' + str(statej) + '.dres'
    file3 = nucleus + '_obdm' + str(statej) + '.dat'

    preprocess(file1, file2 ,statej=statej, statei=statei)
    dres2dat(file2, file3, isospin=False)


if __name__ == "__main__":
    # nucleus = 'I127'
    # for j in range(2,7):
    #     main(nucleus, j)

    nucleus = 'c12'
    main(nucleus, 13)