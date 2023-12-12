#!/usr/bin/env python3
import sys
import argparse

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
        

def translate_line(line: str, offs: int):
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
                new_fret_i = cur_fret_i + offs
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
    output = ""
    for i in range(len(new)):
        next_c = new[i]
        if len(last) == len(new):
            if last[i] != '-':
                next_c = last[i]
        output = output + next_c
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='gtranspose', description='transpose guitar tab by offset')
    parser.add_argument('filename')
    parser.add_argument('offset')
    args = parser.parse_args()
    try:
        offs = int(args.offset)
        with open(args.filename, 'r') as f:
            lines = f.readlines()
            last_line_input = ""
            for l in lines:
                new_line,next_line_input = translate_line(l, offs)
                new_line = merge(last_line_input, new_line)
                print(new_line)
                last_line_input = next_line_input
    except FileNotFoundError as e:
        print("Must provide input file: {}", e)
