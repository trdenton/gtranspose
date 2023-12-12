#!/usr/bin/env python3
import sys

def translate_line(line: str):
    #notes = line.split("-")
    cur_fret = ""
    out_string = ""
    for l in line:
        if l.isnumeric():
            cur_fret = cur_fret + l
        else:
            # not numeric
            # do the processing
            if cur_fret != "":
                old_fret = cur_fret
                cur_fret_i = int(cur_fret)
                cur_fret_i -= 12
                new_fret = str(cur_fret_i)
                if new_fret[0] == '-':
                    new_fret = 'V'+new_fret[1:]
                if len(new_fret) < len(old_fret):
                    new_fret = '-' +new_fret
                out_string = out_string + new_fret
            out_string = out_string + l
            cur_fret = ""
    return out_string.rstrip()

def merge(last: str, new: str):
    
    return (last,new)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        last_line = ""
        for l in lines:
            new_line = translate_line(l)
            if 'V' in last_line:
                last_line,new_line = merge(last_line, new_line)
            print(new_line)
            last_line = new_line
