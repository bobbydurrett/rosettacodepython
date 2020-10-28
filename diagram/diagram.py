"""
http://rosettacode.org/wiki/ASCII_art_diagram_converter

Python example based off Go example:

http://rosettacode.org/wiki/ASCII_art_diagram_converter#Go

"""

def validate(diagram):

    # trim empty lines
    
    rawlines = diagram.splitlines()
    lines = []
    for line in rawlines:
        if line != '':
            lines.append(line)
            
    # validate non-empty lines
            
    if len(lines) == 0:
        print('diagram has no non-empty lines!')
        return None
        
    width = len(lines[0])
    cols = (width - 1) // 3
    
    if cols not in [8, 16, 32, 64]: 
        print('number of columns should be 8, 16, 32 or 64')
        return None
        
    if len(lines)%2 == 0:
        print('number of non-empty lines should be odd')
        return None
    
    if lines[0] != (('+--' * cols)+'+'):
            print('incorrect header line')
            return None

    for i in range(len(lines)):
        line=lines[i]
        if i == 0:
            continue
        elif i%2 == 0:
            if line != lines[0]:
                print('incorrect separator line')
                return None
        elif len(line) != width:
            print('inconsistent line widths')
            return None
        elif line[0] != '|' or line[width-1] != '|':
            print("non-separator lines must begin and end with '|'")    
            return None
    
    return lines


diagram = """
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                      ID                       |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    QDCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ANCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    NSCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ARCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

"""

lines = validate(diagram)

if lines == None:
    print("No lines returned")
else:
    for i in range(len(lines)):
        print(lines[i]+':line '+str(i+1))
    