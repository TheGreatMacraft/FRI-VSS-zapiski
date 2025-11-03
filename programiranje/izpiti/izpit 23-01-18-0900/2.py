import unittest
import random
import warnings
import os


A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

proto_zemljevid = {
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}

zemljevid = {k: set(v.split()) for k, v in proto_zemljevid.items()} | {k[::-1]: set(v.split()) for k, v in
                                                                       proto_zemljevid.items()}

def najzahtevnejse(zemljevid):
    ovire = {}
    for (a,b),value in zemljevid:
        for i in (a,b):
            if(i not in ovire):
                ovire[i] = []
            if(value not in ovire[i]):
                ovire[i].append(value)
    max = 0
    krizisce = ""
    for key,value in ovire:
        if(sum(ovire[key]) > max):
            krizisce = key

    return krizisce

print(najzahtevnejse(proto_zemljevid))