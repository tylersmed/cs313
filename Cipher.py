
import sys
import math

def crt_padded_enc(strng):
    # creates a version of the string to be encoded as a padded message
    sqr_len = math.ceil(math.sqrt(len(strng)))
    paddded_msg = [['*' for x in range(sqr_len)] for i in range(sqr_len)]
    chr_lst = list(strng)

    for row in range(sqr_len):
        for col in range(sqr_len):
            if not chr_lst:
                break
            else:
                paddded_msg[row][col] = chr_lst.pop(0)

    return paddded_msg

def crt_padded_dec(strng):
    # Creates a version of the string to be dectypted as a padded message
    sqr_len = math.ceil(math.sqrt(len(strng)))
    padded_msg = [['*' for x in range(sqr_len)] for i in range(sqr_len)]
    chr_lst = list(strng)
    x = math.ceil(len(chr_lst) / sqr_len)

    for col in range(sqr_len):
        for i in range(x):
            if not chr_lst:
                break
            else:
                padded_msg[col].remove('*')
                padded_msg[col] += [chr_lst.pop(0)]

    return padded_msg

def rotate_right(msg):
    
    lst = []
    if len(msg[1]) == 1:
        lst = [msg[row][0] for row in range(len(msg)-1, -1, -1)]
        return lst

    else:
        lst = [msg[row][0] for row in range(len(msg)-1, -1, -1)]
        for i in range(len(msg)):
            msg[i].pop(0)
        return lst + rotate_right(msg)

def rotate_left(msg):

    lst = []
    if len(msg[1]) == 1:
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
    paddded_msg = crt_padded_dec(strng)
    rotated_msg = rotate_left(paddded_msg)

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
    print(P, Q)

    # encrypt the string P
    print(encrypt(P), end = ' ')

    # decrypt the string Q
    print(decrypt(Q))

    # print the encrypted string of P
    # and the decrypted string of Q

     
if __name__ == "__main__":
    main()
