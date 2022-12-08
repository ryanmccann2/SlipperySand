#!/usr/bin/env python3

# Team Name = SlipperySand
# Team Member = Ryan McCann
# Theory of Computing Project #3, fa22
# trace program for NTM

from traceTM_SlipperySand import TuringMachine
import csv

STEP_LIMIT = 1000

def main():
    ''' Initializing turing machine for aplus, caesar cipher, and contains double b '''
    # aplus
    tm_aplus = TuringMachine()
    tm_aplus.getMachine("aplus.csv")
    
    aplusHistory_accept, aplusConfigs_accept, aplus_max_step_accept = tm_aplus.trace("aaa", STEP_LIMIT)
    aplusHistory_reject, aplusConfigs_reject, aplus_max_step_reject = tm_aplus.trace("bbb", STEP_LIMIT)
    aplusHistory_ms, aplusConfigs_ms, aplus_max_step_ms = tm_aplus.trace("_________________a", 3)

    # caesar cipher
    tm_caesar_cipher = TuringMachine()
    tm_caesar_cipher.getMachine("caesar_cipher.csv")
    
    ccHistory_accept, ccConfigs_accept, cc_max_step_accept = tm_caesar_cipher.trace("2abcd", STEP_LIMIT)
    ccHistory_reject, ccConfigs_reject, cc_max_step_reject = tm_caesar_cipher.trace("2ab5cd", STEP_LIMIT)
    ccHistory_ms, ccConfigs_ms, cc_max_step_ms = tm_caesar_cipher.trace("2abcd", 1)

    # contains double B
    tm_doubleB = TuringMachine()
    tm_doubleB.getMachine("containsdoubleb.csv")

    bbHistory_accept, bbConfigs_accept, bb_max_step_accept = tm_doubleB.trace("aaaaaabbaaa", STEP_LIMIT)
    bbHistory_reject, bbConfigs_reject, bb_max_step_reject = tm_doubleB.trace("aaaaabaa", STEP_LIMIT)
    bbHistory_ms, bbConfigs_ms, bb_max_step_ms = tm_doubleB.trace("aaabaaaaaaabb", 2)

    ''' write to files '''
    # write to aplus
    aplus = open("aplus.txt", "a")
    aplus.write("Aplus Accepted\n")
    aplus.write(f'String = "aaa" was accepted in {len(aplusHistory_accept.split(","))-1} transitions.\n')
    aplus.write("Configurations:\n")
    for c in aplusConfigs_accept:
        aplus.write("%s\n" % c)
    aplus.write("\n")

    aplus.write("Aplus Rejected\n")
    aplus.write(f'String = "bbb" was rejected in {aplus_max_step_reject} steps.\n')
    aplus.write("\n")

    aplus.write("Aplus Max Step Limit\n")
    aplus.write(f'Execution stopped after 3 steps.\n')
    aplus.write("\n")

    # close file
    aplus.close()

    # write to caesar cipher
    cc = open("caesar_cipher.txt", "a")
    cc.write("Caesar Cipher Accpeted\n")
    cc.write(f'String = "2abcd" was accepted in {len(ccHistory_accept.split(","))-1} transitions.\n')
    cc.write("Configurations:\n")
    for c in ccConfigs_accept:
        cc.write("%s\n" % c)
    cc.write("\n")

    cc.write("Caesar Cipher Rejected\n")
    cc.write(f'String = "2ab5cd" was rejected in {cc_max_step_reject} steps.\n')
    cc.write("\n")

    cc.write("Caesar Cipher Max Step Limit\n")
    cc.write(f'Execution stopped after 1 steps.\n')
    cc.write("\n")

    # close file
    cc.close()


    # write to conatains_double B
    bb = open("BB.txt", "a")
    bb.write("Contains Double B Accepted\n")
    bb.write(f'String = "aaaaaabbaaa" was accepted in {len(bbHistory_accept.split(","))-1} transitions.\n')
    bb.write("Configurations:\n")
    for c in bbConfigs_accept:
        bb.write("%s\n" % c)
    bb.write("\n")

    bb.write("Contains Double B Rejected\n")
    bb.write(f'String = "aaaaabaa" was rejected in {bb_max_step_reject} steps.\n')
    bb.write("\n")

    bb.write("Contains Double B Max Step Exceeded\n")
    bb.write(f'Execution stopped after 2 steps.\n')
    bb.write("\n")

    # close file
    bb.close()

if __name__ == "__main__":
    main()