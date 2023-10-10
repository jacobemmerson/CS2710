#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Propositional_KB_agent import *

def check_rules(KB, check, k): # k is for error checking
    for rule in KB.RB: # look for a rule where the conc. == check (when k = 0, theorem)
        all_conds_good = 1
        if check == rule.then_part: # found 
            print(f"Checking [{check}] with {rule.name}: {rule.cond_part} (level = {k})")
            for c in rule.cond_part: # check the conditions
                if c not in KB.FB: # if condition is not known, check for the condition in rules
                    if check_rules(KB, c, k + 1): #if eventually satisfied, return True
                        if rule.cond_part[-1] == c: # is this the last condition
                            print(f"Satsified {rule.name}: {rule.cond_part}\nAdding: {rule.then_part}\n")
                            KB.add_fact(rule.then_part)
                            return True

                        else:
                            continue
                    # if condition is not satisfied, check another rule
                    all_conds_good = 0
                    print(f"Failed to Satisfy {rule.name}: {rule.cond_part}\n")
                    break

            if all_conds_good == 1:
                print(f"Satsified {rule.name}: {rule.cond_part}\nAdding: {rule.then_part}\n")
                KB.add_fact(rule.then_part)
                return True

    # return false if no rule found 
    return False

def backwardchain(KB, theorem):
    base = KB
    base.reset_FB(init_FB)
    to_prove = theorem

    if to_prove in base.FB:
        print("Theorem already Known\n")
        print("Facts:")
        base.print_FB()
        return True

    t = check_rules(base, to_prove, k = 0)

    print(f"\n\nFacts (n = {len(base.FB)}):")
    base.print_FB()
    return t


print(f"Testing Theorem 1: {theorem1}")
print(f"Theorem is {backwardchain(KBase, theorem1)}\n\n")

print(f"Testing Theorem 2: {theorem2}")
print(f"Theorem is {backwardchain(KBase, theorem2)}\n\n")

print(f"Testing Theorem 3: {theorem3}")
print(f"Theorem is {backwardchain(KBase, theorem3)}\n\n")

print(f"Testing Theorem 4: {theorem4}")
print(f"Theorem is {backwardchain(KBase, theorem4)}\n\n")

print(f"Testing Theorem 5: {theorem5}")
print(f"Theorem is {backwardchain(KBase, theorem5)}\n\n")