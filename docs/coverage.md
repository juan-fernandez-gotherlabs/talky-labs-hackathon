# Policy coverage audit

This is an executable inventory for M0, not an implemented accounting engine. Issues #32 and #35 remain teammate integration dependencies. M1–M7 rows are planned. Policy conventions are delivered as a documented M0 contract; downstream rule execution remains planned. Golden examples are audit/evaluation evidence only.

Reproduce: `PYTHONPATH=src python3 -m unittest discover -s tests -p test_coverage.py`. Raw evidence: participant.zip SHA-256 c813449eab9ddc7fc28b04eff85518957035e895b5500fd19e26c0d8ef7f0109. Every policy bullet/table rule in §§1–6 has a stable ID and source line. No observed code proves every boundary condition. Rows without directly keyed golden evidence require targeted tests.

| Rule | Source | Issues | July evidence | Status |
|---|---|---|---|---|
| P1-01 | POLITICAS_CONTABLES.md:7 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-02 | POLITICAS_CONTABLES.md:8 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-03 | POLITICAS_CONTABLES.md:9 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-04 | POLITICAS_CONTABLES.md:10 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-05 | POLITICAS_CONTABLES.md:11 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-06 | POLITICAS_CONTABLES.md:12 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-07 | POLITICAS_CONTABLES.md:13 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P1-08 | POLITICAS_CONTABLES.md:14 | #29, #30, #31 | 0 keyed cases; requires_evidence_or_synthetic_test | m0_delivered |
| P2-01 | POLITICAS_CONTABLES.md:22 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 308 keyed cases; observed | planned |
| P2-02 | POLITICAS_CONTABLES.md:23 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 242 keyed cases; observed | planned |
| P2-03 | POLITICAS_CONTABLES.md:24 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 242 keyed cases; observed | planned |
| P2-04 | POLITICAS_CONTABLES.md:25 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 12 keyed cases; observed | planned |
| P2-05 | POLITICAS_CONTABLES.md:26 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 12 keyed cases; observed | planned |
| P2-06 | POLITICAS_CONTABLES.md:27 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 12 keyed cases; observed | planned |
| P2-07 | POLITICAS_CONTABLES.md:28 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 12 keyed cases; observed | planned |
| P2-08 | POLITICAS_CONTABLES.md:29 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 12 keyed cases; observed | planned |
| P2-09 | POLITICAS_CONTABLES.md:30 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 12 keyed cases; observed | planned |
| P2-10 | POLITICAS_CONTABLES.md:36 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 14 keyed cases; observed | planned |
| P2-11 | POLITICAS_CONTABLES.md:37 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 18 keyed cases; observed | planned |
| P2-12 | POLITICAS_CONTABLES.md:46 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 19 keyed cases; observed | planned |
| P2-13 | POLITICAS_CONTABLES.md:51 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-14 | POLITICAS_CONTABLES.md:52 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 242 keyed cases; observed | planned |
| P2-15 | POLITICAS_CONTABLES.md:56 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-16 | POLITICAS_CONTABLES.md:57 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-17 | POLITICAS_CONTABLES.md:58 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-18 | POLITICAS_CONTABLES.md:62 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-19 | POLITICAS_CONTABLES.md:63 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-20 | POLITICAS_CONTABLES.md:64 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-21 | POLITICAS_CONTABLES.md:65 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-22 | POLITICAS_CONTABLES.md:66 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-23 | POLITICAS_CONTABLES.md:67 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-24 | POLITICAS_CONTABLES.md:68 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-25 | POLITICAS_CONTABLES.md:69 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-26 | POLITICAS_CONTABLES.md:70 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-27 | POLITICAS_CONTABLES.md:71 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-28 | POLITICAS_CONTABLES.md:72 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-29 | POLITICAS_CONTABLES.md:73 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-30 | POLITICAS_CONTABLES.md:74 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P2-31 | POLITICAS_CONTABLES.md:75 | #39, #40, #41, #42, #43, #44, #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-01 | POLITICAS_CONTABLES.md:81 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-02 | POLITICAS_CONTABLES.md:82 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-03 | POLITICAS_CONTABLES.md:83 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-04 | POLITICAS_CONTABLES.md:84 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 1 keyed cases; observed | planned |
| P3-05 | POLITICAS_CONTABLES.md:85 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-06 | POLITICAS_CONTABLES.md:86 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-07 | POLITICAS_CONTABLES.md:87 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-08 | POLITICAS_CONTABLES.md:88 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-09 | POLITICAS_CONTABLES.md:89 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-10 | POLITICAS_CONTABLES.md:90 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-11 | POLITICAS_CONTABLES.md:91 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-12 | POLITICAS_CONTABLES.md:92 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-13 | POLITICAS_CONTABLES.md:95 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-14 | POLITICAS_CONTABLES.md:96 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-15 | POLITICAS_CONTABLES.md:97 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-16 | POLITICAS_CONTABLES.md:98 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-17 | POLITICAS_CONTABLES.md:99 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-18 | POLITICAS_CONTABLES.md:100 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-19 | POLITICAS_CONTABLES.md:101 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-20 | POLITICAS_CONTABLES.md:102 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-21 | POLITICAS_CONTABLES.md:103 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-22 | POLITICAS_CONTABLES.md:104 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-23 | POLITICAS_CONTABLES.md:110 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-24 | POLITICAS_CONTABLES.md:111 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P3-25 | POLITICAS_CONTABLES.md:112 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 1 keyed cases; observed | planned |
| P3-26 | POLITICAS_CONTABLES.md:113 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 1 keyed cases; observed | planned |
| P3-27 | POLITICAS_CONTABLES.md:114 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 1 keyed cases; observed | planned |
| P3-28 | POLITICAS_CONTABLES.md:115 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 2 keyed cases; observed | planned |
| P3-29 | POLITICAS_CONTABLES.md:116 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 2 keyed cases; observed | planned |
| P3-30 | POLITICAS_CONTABLES.md:117 | #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #78, #79, #80, #81, #82, #83, #84, #85, #86, #87 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P4-01 | POLITICAS_CONTABLES.md:123 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P4-02 | POLITICAS_CONTABLES.md:124 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P4-03 | POLITICAS_CONTABLES.md:128 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 12 keyed cases; observed | planned |
| P4-04 | POLITICAS_CONTABLES.md:129 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 2 keyed cases; observed | planned |
| P4-05 | POLITICAS_CONTABLES.md:130 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-06 | POLITICAS_CONTABLES.md:131 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-07 | POLITICAS_CONTABLES.md:132 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 3 keyed cases; observed | planned |
| P4-08 | POLITICAS_CONTABLES.md:133 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-09 | POLITICAS_CONTABLES.md:134 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 2 keyed cases; observed | planned |
| P4-10 | POLITICAS_CONTABLES.md:135 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-11 | POLITICAS_CONTABLES.md:136 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 2 keyed cases; observed | planned |
| P4-12 | POLITICAS_CONTABLES.md:137 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-13 | POLITICAS_CONTABLES.md:138 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P4-14 | POLITICAS_CONTABLES.md:139 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 2 keyed cases; observed | planned |
| P4-15 | POLITICAS_CONTABLES.md:140 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-16 | POLITICAS_CONTABLES.md:141 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-17 | POLITICAS_CONTABLES.md:142 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-18 | POLITICAS_CONTABLES.md:143 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P4-19 | POLITICAS_CONTABLES.md:144 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 3 keyed cases; observed | planned |
| P4-20 | POLITICAS_CONTABLES.md:145 | #66, #67, #68, #69, #70, #71, #72, #73, #74, #75, #76, #77 | 1 keyed cases; observed | planned |
| P5-01 | POLITICAS_CONTABLES.md:149 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 57 keyed cases; observed | planned |
| P5-02 | POLITICAS_CONTABLES.md:150 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-03 | POLITICAS_CONTABLES.md:151 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-04 | POLITICAS_CONTABLES.md:152 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-05 | POLITICAS_CONTABLES.md:153 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-06 | POLITICAS_CONTABLES.md:154 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 9 keyed cases; observed | planned |
| P5-07 | POLITICAS_CONTABLES.md:155 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-08 | POLITICAS_CONTABLES.md:156 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-09 | POLITICAS_CONTABLES.md:157 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-10 | POLITICAS_CONTABLES.md:158 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 1 keyed cases; observed | planned |
| P5-11 | POLITICAS_CONTABLES.md:159 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-12 | POLITICAS_CONTABLES.md:160 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 8 keyed cases; observed | planned |
| P5-13 | POLITICAS_CONTABLES.md:161 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-14 | POLITICAS_CONTABLES.md:162 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-15 | POLITICAS_CONTABLES.md:163 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-16 | POLITICAS_CONTABLES.md:164 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 1 keyed cases; observed | planned |
| P5-17 | POLITICAS_CONTABLES.md:165 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-18 | POLITICAS_CONTABLES.md:166 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-19 | POLITICAS_CONTABLES.md:167 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-20 | POLITICAS_CONTABLES.md:168 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P5-21 | POLITICAS_CONTABLES.md:169 | #95, #96, #97, #98, #99, #100, #101, #102, #103, #104 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P6-01 | POLITICAS_CONTABLES.md:173 | #88, #89, #90, #91, #92, #93, #94 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P6-02 | POLITICAS_CONTABLES.md:174 | #88, #89, #90, #91, #92, #93, #94 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P6-03 | POLITICAS_CONTABLES.md:175 | #88, #89, #90, #91, #92, #93, #94 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P6-04 | POLITICAS_CONTABLES.md:176 | #88, #89, #90, #91, #92, #93, #94 | 0 keyed cases; requires_evidence_or_synthetic_test | planned |
| P6-05 | POLITICAS_CONTABLES.md:180 | #88, #89, #90, #91, #92, #93, #94 | 1 keyed cases; observed | planned |
| P6-06 | POLITICAS_CONTABLES.md:181 | #88, #89, #90, #91, #92, #93, #94 | 1 keyed cases; observed | planned |
| P6-07 | POLITICAS_CONTABLES.md:182 | #88, #89, #90, #91, #92, #93, #94 | 1 keyed cases; observed | planned |
| P6-08 | POLITICAS_CONTABLES.md:183 | #88, #89, #90, #91, #92, #93, #94 | 1 keyed cases; observed | planned |
| P6-09 | POLITICAS_CONTABLES.md:184 | #88, #89, #90, #91, #92, #93, #94 | 2 keyed cases; observed | planned |
| VAR-POST_PAYMENT_BLOCK | roadmap-auditado.md §5 | #46, #50, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-TAX_GARNISHMENT_ORDER | roadmap-auditado.md §5 | #40, #46, #50, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-REGISTER_EMBARGO | roadmap-auditado.md §5 | #40, #46, #50, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-AEAT_EMBARGO | roadmap-auditado.md §5 | #46, #50, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-BOOK_AMOUNT_ERROR | roadmap-auditado.md §5 | #73, #77, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-DOUBTFUL_RECLASS | roadmap-auditado.md §5 | #101, #102, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-UNOBSERVED_TAX_CODES | roadmap-auditado.md §5 | #29, #52, #53, #63, #109 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-NON_CUSTOMER_INSURANCE | roadmap-auditado.md §5 | #84 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-PREPAID_INITIAL_DEFERRAL | roadmap-auditado.md §5 | #98 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-BAD_DEBT_REVERSAL | roadmap-auditado.md §5 | #101 | 0 keyed cases; unobserved_required_variant | planned |
| VAR-GBP_COMBINATIONS | roadmap-auditado.md §5 | #31, #54, #100 | 0 keyed cases; unobserved_required_variant | planned |

Observed enum/category inventory is in coverage.json, including individual July identifiers. Required variants include certificate expiry, embargo, BOOK_AMOUNT_ERROR, new insolvency/reclassification, unobserved tax codes, insurance receipts, initial deferral, impairment reversals and GBP combinations. Each synthetic case must test the behavior independently of July golden.

Detailed reason-code rows added to executable inventory: P-DETAIL-12, P-DETAIL-22, P-DETAIL-28, P-DETAIL-38, P-DETAIL-39, P-DETAIL-40, P-DETAIL-41, P-DETAIL-42, P-DETAIL-43, P-DETAIL-44, P-DETAIL-45, P-DETAIL-47, P-DETAIL-48, P-DETAIL-49, P-DETAIL-50, P-DETAIL-51, P-DETAIL-68, P-DETAIL-70, P-DETAIL-72, P-DETAIL-87, P-DETAIL-89.
