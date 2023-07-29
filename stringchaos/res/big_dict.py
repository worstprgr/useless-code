#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from stringchaos.core.utils import Utils

u = Utils()

# buckets
b1 = u.lookup_hostname('217.160.0.38')
b2 = u.lookup_hostname('216.58.212.142')
b3 = u.lookup_hostname('2.20.149.130')
b4 = u.lookup_hostname('157.240.223.174')
b5 = u.missing_register()

# registers
register_l_dict = {
    'A0': b1[15],
    'A1': b4[27],
    'A2': b1[19],
    'B0': b3[14],
    'B1': b1[13],
    'B2': b2[12],
    'C0': b3[42],
    'C1': b3[37],
    'C2': b1[18],
    'D0': b5[13],
    'D1': b3[29],
    'D2': b1[14],
    'E0': b1[32],
    'E1': b2[10],
    'E2': b1[31],
    'F0': b3[16],
    'F1': b5[17],
    'F2': b1[28],
    'G0': b1[16],
    'G1': b1[17],
    'G2': b1[25],
    'H0': b4[16],
    'H1': b5[24],
    'H2': b5[5],
    'I0': b3[19],
    'I1': b5[12]
}

register_u_dict = u.bigd_gen_upper(register_l_dict)
register_s_dict = u.bigd_gen_special([register_l_dict, register_u_dict])
