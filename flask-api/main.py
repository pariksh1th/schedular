# Strictly for 3rd, 5th and 7th semester CSE



#for _ in timetable:
# print(timetable) s
def returnTable(user):
    global test_user 
    test_user = user
    from SEM3CSEA import ttCSE3A
    from SEM3CSEB import ttCSE3B
    from SEM5CSEA import tt5CSA
    from SEM5CSEB import tt5CSB
    from SEM7 import timetable7
    from SEM3ECE import ttECE3
    from SEM5ECE import tt5ECE
    from SEM7ECE import ttECE7
    from SEM3DS import ttDS3
    from SEM5DS import tt5DS, teachers


    timetable = { 'CSE3A' : ttCSE3A,
                'CSE3B' : ttCSE3B,
                'CSE5A' : tt5CSA,
                'CSE5B' : tt5CSB,
                'CSESEM7': timetable7,
                'ECESEC3': ttECE3,
                'ECESEM5': tt5ECE,
                'ECESEM7': ttECE7,
                'DSSEM3': ttDS3,
                'DDSEM5': tt5DS,
                "teachers": teachers
    }
    print("done")

    return timetable


