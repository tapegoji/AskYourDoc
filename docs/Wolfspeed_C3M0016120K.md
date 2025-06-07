# Wolfspeed_C3M0016120K

*Document converted on 2025-05-04*

## Table 1

|    | Ordering Part Number   | Package   | Marking     |
|---:|:-----------------------|:----------|:------------|
|  0 | C3M0016120K            | TO 247-4  | C3M0016120K |

## Table 2

|    | Parameter                                  | Symbol     | Min.   | Typ.   | Max         | Unit      | Conditions                                       | Note           |
|---:|:-------------------------------------------|:-----------|:-------|:-------|:------------|:----------|:-------------------------------------------------|:---------------|
|  0 | Drain - Source Voltage                     | V DS       |        |        | 1200        | V         | T C = 25°C                                       |                |
|  1 | Maximum Gate - Source Voltage              | V GS(max)  | -8     |        | +19         | V         | Transient                                        |                |
|  2 | Operational Gate-Source Voltage            | V GS op    |        | -4/15  |             | V         | Static                                           | Note 1         |
|  3 | DC Continuous Drain Current                | I D        |        |        | 115         | A         | V GS = 15 V, T C = 25 °C, T J ≤175 °C            | Fig. 19 Note 2 |
|  4 | DC Continuous Drain Current                | I D        |        |        | 85          | A         | V GS = 15 V, T C = 100 °C, T J ≤175 °C           |                |
|  5 | Pulsed Drain Current                       | I DM       |        |        | 250         | A         | t Pmax limited by T jmax V GS = 15V, T C = 25 °C | Fig. 22        |
|  6 | Power Dissipation                          | P D        |        |        | 556         | W         | T C = 25˚C, T J = 175 °C                         | Fig. 20        |
|  7 | Operating Junction and Storage Temperature | T, J T stg |        |        | -40 to +175 | °C        |                                                  |                |
|  8 | Solder Temperature                         | T L        |        |        | 260         | °C        | According to JEDEC J-STD-020                     |                |
|  9 | Mounting Torque                            | M D        |        |        | 1 8.8       | Nm Ibf-in | M3or 6-32 screw                                  |                |

## Table 3

|    | Parameter                                  | Symbol    | Min.   | Typ.   | Max.   | Unit   | Test Conditions                                                                                                    | Note         |
|---:|:-------------------------------------------|:----------|:-------|:-------|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------|:-------------|
|  0 | Drain-Source Breakdown Voltage             | V (BR)DSS | 1200   | -      | -      | V      | V GS = 0 V, I D = 100 μA                                                                                           | Fig. 11      |
|  1 | Gate Threshold Voltage                     | V GS(th)  | 1.8    | 2.5    | 3.6    | V      | V DS = V GS, I D = 23 mA                                                                                           | Fig. 11      |
|  2 |                                            | V GS(th)  | -      | 2.0    | -      | V      | V DS = V GS, I D = 23 mA, T J = 175°C                                                                              | Fig. 11      |
|  3 | Zero Gate Voltage Drain Current            | I DSS     | -      | 1      | 50     | μA     | V DS = 1200 V, V GS = 0 V                                                                                          |              |
|  4 | Gate-Source Leakage Current                | I GSS     | -      | 10     | 250    | μA     | V GS = 15 V, V DS = 0 V                                                                                            |              |
|  5 | Drain-Source On-State Resistance           | R DS(on)  | -      | 16     | 22.3   | mΩ     | V GS = 15 V, I D = 75 A                                                                                            | Fig. 4, 5, 6 |
|  6 |                                            | R DS(on)  | -      | 28.8   | -      | mΩ     | V GS = 15 V, I D = 75 A, T J = 175°C                                                                               | Fig. 4, 5, 6 |
|  7 | Transconductance                           | g fs      | -      | 53     | -      | S      | V DS = 20 V, I DS = 75 A                                                                                           | Fig. 7       |
|  8 |                                            | g fs      | -      | 47     | -      | S      | V DS = 20 V, I DS = 75 A, T J = 175°C                                                                              | Fig. 7       |
|  9 | Input Capacitance                          | C iss     | -      | 6085   | -      | pF     | V GS = 0 V, V DS = 1000 V ƒ = 100 khz V = 25 mV                                                                    | Fig. 17, 18  |
| 10 | Output Capacitance                         | C oss     | -      | 230    | -      | pF     | V GS = 0 V, V DS = 1000 V ƒ = 100 khz V = 25 mV                                                                    | Fig. 17, 18  |
| 11 | Reverse Transfer Capacitance               | C rss     | -      | 13     | -      | pF     | AC                                                                                                                 | Fig. 17, 18  |
| 12 | C oss Stored Energy                        | E oss     | -      | 130    | -      | μJ     | V GS = 0 V, V DS = 1000 V ƒ = 100 khz V = 25 mV                                                                    | Fig. 16      |
| 13 | Turn-On Switching Energy (SiC Diode FWD)   | E on      | -      | 1.1    | -      | mJ     | V DS = 800 V, V GS = -4 V/+15 V, I D = 75 A, R G(ext) = 2.5 Ω, L= 65.7 μH, T J = 175ºC                             | Fig. 26      |
| 14 | Turn Off Switching Energy (SiC Diode FWD)  | E off     | -      | 0.8    | -      | mJ     | V DS = 800 V, V GS = -4 V/+15 V, I D = 75 A, R G(ext) = 2.5 Ω, L= 65.7 μH, T J = 175ºC                             | Fig. 26      |
| 15 | Turn-On Switching Energy (Body Diode FWD)  | E on      | -      | 2.3    | -      | mJ     | V DS = 800 V, V GS = -4 V/+15 V, I D = 75 A, R G(ext) = 2.5 Ω, L= 65.7 μH, T J = 175ºC                             | Fig. 26      |
| 16 | Turn Off Switching Energy (Body Diode FWD) | E off     | -      | 0.6    | -      | mJ     | V DS = 800 V, V GS = -4 V/+15 V, I D = 75 A, R G(ext) = 2.5 Ω, L= 65.7 μH, T J = 175ºC                             | Fig. 26      |
| 17 | Turn-On Delay Time                         | t d(on)   | -      | 34     | -      | ns     | V DD = 800 V, V GS = -4 V/15 V R G(ext) = 2.5 Ω, I D = 75 A, L = 65.7 μH, Timing relative to V DS , Inductive load | Fig. 27      |
| 18 | Rise Time                                  | t r       | -      | 33     | -      | ns     | V DD = 800 V, V GS = -4 V/15 V R G(ext) = 2.5 Ω, I D = 75 A, L = 65.7 μH, Timing relative to V DS , Inductive load | Fig. 27      |
| 19 | Turn-Off Delay Time                        | t d(off)  | -      | 65     | -      | ns     | V DD = 800 V, V GS = -4 V/15 V R G(ext) = 2.5 Ω, I D = 75 A, L = 65.7 μH, Timing relative to V DS , Inductive load | Fig. 27      |
| 20 | Fall Time                                  | t f       | -      | 13     | -      | ns     | V DD = 800 V, V GS = -4 V/15 V R G(ext) = 2.5 Ω, I D = 75 A, L = 65.7 μH, Timing relative to V DS , Inductive load | Fig. 27      |
| 21 | Internal Gate Resistance                   | R G(int)  | -      | 2.6    | -      | Ω      | ƒ = 1 MHz, V AC = 25 mV                                                                                            |              |
| 22 | Gate to Source Charge                      | Q gs      | -      | 67     | -      | nC     | V DS = 800 V, V GS = -4 V/15 V I D = 75 A Per IEC60747-8-4 pg 21                                                   | Fig. 12      |
| 23 | Gate to Drain Charge                       | Q gd      | -      | 61     | -      | nC     | V DS = 800 V, V GS = -4 V/15 V I D = 75 A Per IEC60747-8-4 pg 21                                                   | Fig. 12      |
| 24 | Total Gate Charge                          | Q g       | -      | 211    | -      | nC     | V DS = 800 V, V GS = -4 V/15 V I D = 75 A Per IEC60747-8-4 pg 21                                                   | Fig. 12      |

## Table 4

|    | Parameter                          | Symbol   | Typ.   | Max.   | Unit   | Test Conditions                                                        | Notes      |
|---:|:-----------------------------------|:---------|:-------|:-------|:-------|:-----------------------------------------------------------------------|:-----------|
|  0 | Diode Forward Voltage              | V SD     | 4.6    | -      | V      | V GS = -4 V, I SD = 37.5 A, T J = 25°C                                 | Fig. 8, 9, |
|  1 |                                    | V SD     | 4.2    | -      | V      | V GS = -4 V, I SD = 37.5 A, T J = 175°C                                | 10         |
|  2 | Continuous Diode Forward Current 1 | I S      | -      | 112    | A      | V GS = -4 V, T C = 25°C                                                | Note 3     |
|  3 | Diode Pulse Current                | I SM     | -      | 250    | A      | V GS = -4 V, pulse width t P limited by T j max                        | Note 3     |
|  4 | Reverse Recovery Time              | t rr     | 30     | -      | ns     | V GS = -4 V, I SD = 75 A, V R = 800 V di F /dt = 4000 A/μs T J = 175°C | Note 3     |
|  5 | Reverse Recovery Charge            | Q rr     | 1238   | -      | nC     | V GS = -4 V, I SD = 75 A, V R = 800 V di F /dt = 4000 A/μs T J = 175°C | Note 3     |
|  6 | PeakReverse Recovery Current       | I RRM    | 64     | -      | A      | V GS = -4 V, I SD = 75 A, V R = 800 V di F /dt = 4000 A/μs T J = 175°C | Note 3     |
|  7 | Reverse Recovery Time              | t rr     | 27     | -      | ns     | V GS = -4 V, I SD = 75 A, V R = 800 V di F /dt = 5500 A/μs T J = 175°C | Note 3     |
|  8 | Reverse Recovery Charge            | Q rr     | 1261   | -      | nC     | V GS = -4 V, I SD = 75 A, V R = 800 V di F /dt = 5500 A/μs T J = 175°C | Note 3     |
|  9 | PeakReverse Recovery Current       | I RRM    | 77     | -      | A      | V GS = -4 V, I SD = 75 A, V R = 800 V di F /dt = 5500 A/μs T J = 175°C | Note 3     |

## Table 5

|    | Parameter                                   | Symbol   |   Typ. | Unit   | Test Conditions   | Notes   |
|---:|:--------------------------------------------|:---------|-------:|:-------|:------------------|:--------|
|  0 | Thermal Resistance from Junction to Case    | R θJC    |   0.27 | °C/W   |                   | Fig. 21 |
|  1 | Thermal Resistance from Junction to Ambient | R θJA    |  40    | °C/W   |                   | Fig. 21 |

## Table 6

|    | SYMBOL   | MIN (mm)   | MAX(mm)   |
|---:|:---------|:-----------|:----------|
|  0 | A        | 4.83       | 5.21      |
|  1 | A1       | 2.23       | 2.54      |
|  2 | A2       | 1.91       | 2.16      |
|  3 | b        | 1.07       | 1.33      |
|  4 | b1       | 2.39       | 2.94      |
|  5 | b3       | 1.07       | 1.60      |
|  6 | b7       | 1.30       | 1.70      |
|  7 | b8       | 1.80       | 2.20      |
|  8 | c        | 0.55       | 0.68      |
|  9 | D        | 23.30      | 23.63     |
| 10 | D1       | 16.25      | 17.65     |
| 11 | D2       | 5.55       | 5.95      |
| 12 | E        | 15.75      | 16.13     |
| 13 | E1       | 13.1       | 14.15     |
| 14 | E2       | 3.68       | 5.10      |
| 15 | E3       | 1.00       | 1.90      |
| 16 | E4       | 12.38      | 13.43     |
| 17 | E5       | 14.65      | 15.05     |
| 18 | e1       | 5.08 BSC   | 5.08 BSC  |
| 19 | L        | 17.31      | 17.82     |
| 20 | L1       | 3.97       | 4.37      |
| 21 | L2       | 2.35       | 2.65      |
| 22 | P        | 3.51       | 3.65      |
| 23 | Q        | 5.49       | 6.00      |
| 24 | S        | 6.04       | 6.30      |
| 25 | T        | 17.5 REF.  | 17.5 REF. |
| 26 | W        | 3.5 REF.   | 3.5 REF.  |
| 27 | X        | 4 REF.     | 4 REF.    |

## Table 7

|    |   0 | 1             |
|---:|----:|:--------------|
|  0 |   1 | DRAIN         |
|  1 |   2 | SOURCE        |
|  2 |   3 | DRIVER SOURCE |
|  3 |   4 | GATE          |
|  4 |   5 | DRAIN         |

## Table 8

|    | Document Version   | Date of release   | Description of changes                                                                                         |
|---:|:-------------------|:------------------|:---------------------------------------------------------------------------------------------------------------|
|  0 | -                  | April-2019        | Initial datasheet                                                                                              |
|  1 | 2                  | December-2023     | Update Package Drawing, package image, solder pad layout, added revision history table, Table 1 layout revised |
|  2 | 3                  | March-2024        | RDSON LSL Removed                                                                                              |
|  3 | 4                  | September - 2024  | Legal Disclaimer, POD, Diode Pulse Current Symbol                                                              |

