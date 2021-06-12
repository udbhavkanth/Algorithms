#in this question we have to find that if there is any 
#validate subsequence or not
#in our array

def validateSubsquence (array,sequence):
    arrid = 0
    seqid = 0
    while arrid <len(array) and seqid < len(sequence):
        if array[arrid] == sequence[seqid]:
            seqid += 1
        arrid += 1
    return seqid == len(sequence)

##with For Loop

def validateSubsquence1 (array,sequence):
    seqid = 0
    for value in array:
        if seqid ==  len(sequence):
            break
        if sequence[seqid] == value:
            seqid += 1 
    return seqid == len(sequence)
