#!/usr/bin/python3
def display_board(board, width):
    output=""
    row=""
    j=0
    rows=(len(board) // width)
    for i in range(rows):
        j=i*width
        row=" | ".join(board[j:j+width])
        output+=' '+row+' '
        if i < rows-1:
            output+='\n'+('-'*((width*3)+width-1))+'\n'
    return output
