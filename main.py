#!/usr/bin/env python3
import sys

def get_next_string(note):
    if note == 'e':
        return 'B'
    if note == 'B':
        return 'G'
    if note == 'G':
        return 'D'
    if note == 'D':
        return 'A'
    if note == 'A':
        return 'E'
    return '?'
        

def translate_line(line: str):
    #notes = line.split("-")
    note = line[0]
    offset_fret_next_string = 5
    next_string_note = get_next_string(note)
    if note == 'B':
        offset_fret_next_string = 4
    
    cur_fret = ""
    out_string = ""
    next_string_line = ""
    for l in line:
        if l.isnumeric():
            cur_fret = cur_fret + l
        else:
            # not numeric
            # do the processing
            if cur_fret != "":
                old_fret = cur_fret
                cur_fret_i = int(cur_fret)
                new_fret_i = cur_fret_i - 12
                new_fret = str(new_fret_i)
                next_string_fret = '-'*len(old_fret)
                if new_fret_i < 0:
                    new_fret = '-'*len(old_fret)
                    next_string_fret = str(new_fret_i + offset_fret_next_string)
                if len(new_fret) < len(old_fret):
                    new_fret = '-' +new_fret
                if len(next_string_fret) < len(old_fret):
                    next_string_fret = "-" + next_string_fret
                out_string = out_string + new_fret
                next_string_line = next_string_line + next_string_fret

            out_string = out_string + l
            next_string_line = next_string_line + l
            cur_fret = ""
    next_string_line = next_string_note + next_string_line[1:]
    return out_string.rstrip(), next_string_line.rstrip()

def merge(last: str, new: str):
    
    return (last,new)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        last_line = ""
        for l in lines:
            new_line,next_string = translate_line(l)
            print (new_line)
            print (next_string)
