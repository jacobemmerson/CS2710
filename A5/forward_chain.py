#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Propositional_KB_agent import *

def check_all_conditions(rule, facts):
    for c in rule.cond_part:
        if c not in facts:
            return False
    return True

def forwardchain(KB, theorem):
    base = KB
    to_prove = theorem
    rules = base.RB

    if to_prove in base.FB:
        print("Theorem already Known\n")
        print(f"Facts (n = {len(base.FB)}):")
        base.print_FB()
        return True

    fact_added = 1
    while fact_added:
        fact_added = 0 # reset
        facts = base.FB # in case facts are updated
        for rule in rules:
            if base.is_in_FB(rule.then_part): # skip checking for facts we already know
                continue

            if check_all_conditions(rule, facts): # new fact if all conditions satisfied
                base.add_fact(rule.then_part)
                fact_added = 1
                print(f"Satisfied {rule.name}: {rule.cond_part}")
                print(f"Added: {rule.then_part}\n")
                if rule.then_part == to_prove:
                    print(f"Facts (n = {len(base.FB)}):")
                    base.print_FB()
                    base.reset_FB(init_FB)
                    return True
    print(f"Facts (n = {len(base.FB)}):")
    base.print_FB()
    base.reset_FB(init_FB)
    return False

print(f"Testing Theorem 1: {theorem1}")
print(f"Theorem is {forwardchain(KBase, theorem1)}\n\n")

print(f"Testing Theorem 2: {theorem2}")
print(f"Theorem is {forwardchain(KBase, theorem2)}\n\n")

print(f"Testing Theorem 3: {theorem3}")
print(f"Theorem is {forwardchain(KBase, theorem3)}\n\n")

print(f"Testing Theorem 4: {theorem4}")
print(f"Theorem is {forwardchain(KBase, theorem4)}\n\n")

print(f"Testing Theorem 5: {theorem5}")
print(f"Theorem is {forwardchain(KBase, theorem5)}\n\n")