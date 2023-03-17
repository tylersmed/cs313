
import sys
import math

def crt_padded_enc(strng):
    # creates a version of the string to be encoded as a padded message
    sqr_len = math.ceil(math.sqrt(len(strng)))
    paddded_msg = [['*' for x in range(sqr_len)] for i in range(sqr_len)]
    chr_lst = list(strng)

    for row in range(sqr_len):
        # replaces '*'s with chars from the string in a right to left,
        # top to bottom direction
        for col in range(sqr_len):
            if not chr_lst:
                break
            else:
                paddded_msg[row][col] = chr_lst.pop(0)

    return paddded_msg

def crt_padded_dec(strng):
    # Creates a version of the string to be dectypted as a padded message
    sqr_len = math.ceil(math.sqrt(len(strng)))
    padded_msg = [[0 for x in range(sqr_len)] for i in range(sqr_len)]
    numStars = (sqr_len ** 2) - len(strng)
    chr_lst = list(strng)

    num = 0
    row = -1
    while num < numStars:
        # adds the needed number of '*'s to the matrix in a right to left, bottom to top direction
        padded_msg[row].remove(0)
        padded_msg[row].insert(0, "*")
        num += 1
        row -= 1
        if row < -sqr_len:
            row = -1
    
    for row in range(sqr_len):
        # Adds the charachters in the string to the matrix in a right to left,
        # top to bottom direction while skipping any index that contains '*'.
        for col in range(sqr_len):
            if padded_msg[row][col] == '*':
                continue
            else:
                padded_msg[row][col] = chr_lst.pop(0)    

    return padded_msg

def rotate_right(msg):
    # Takes a padded message and returns it rotated 90 degrees to the right
    lst = []
    if len(msg[0]) == 1:
        lst = [msg[row][0] for row in range(len(msg)-1, -1, -1)]
        return lst

    else:
        lst = [msg[row][0] for row in range(len(msg)-1, -1, -1)]
        for i in range(len(msg)):
            msg[i].pop(0)
        return lst + rotate_right(msg)

def rotate_left(msg):
    # takes a padded message and returns it rotated 90 degrees to the left
    lst = []
    if len(msg[0]) == 1:
        lst = [msg[row][0] for row in range(len(msg))]
        return lst

    else:
        lst = [msg[row][-1] for row in range(len(msg))]
        for i in range(len(msg)):
            msg[i].pop(-1)
        return lst + rotate_left(msg)

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
   
def encrypt ( strng ):
    padded_msg = crt_padded_enc(strng)
    rotated_msg = rotate_right(padded_msg)

    encrypted_msg = ''
    for char in rotated_msg:
        if char == '*':
            continue
        else:
            encrypted_msg += char

    return encrypted_msg

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 

def decrypt ( strng ):
    padded_msg = crt_padded_dec(strng)
    rotated_msg = rotate_left(padded_msg)

    decrypted_msg = ''
    for char in rotated_msg:
        if char == '*':
            continue
        else:
            decrypted_msg += char

    return decrypted_msg

def main():
    # read the strings P and Q from standard input
    P, Q = sys.stdin.read().strip().split("\n")

    # encrypt the string 
    encP = encrypt(P)

    # decrypt the string Q
    decQ = decrypt(Q)

    # print the encrypted string of P
    print(encP)

    # and the decrypted string of Q
    print(decQ)
     
if __name__ == "__main__":
    main()
