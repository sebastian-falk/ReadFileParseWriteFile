import sys
import os
from collections import deque
import uuid

def main():
    filepath = "filepath.txt"

    if not os.path.isfile(filepathFarger) 
       print("File path {} does not exist. Exiting...".format(filepathFarger))
       sys.exit()

    insertScriptsFarger = deque()
    
    with open(filepathFarger) as fp:
        for line in fp:
            # print("contents: {}".format(line))
            insertScriptsFarger.append(createInsertScriptsFarger(line))
    
    filepathWriteFarger = "insert_scripts_for_farger.txt"

    with open(filepathWriteFarger, 'w') as fpw:
        fpw.writelines(insertScriptsFarger)

def createInsertScriptsFarger(line):
    lineArray = line.replace(';', '').split(',')
    insertScript = "INSERT INTO ileggelse.farge(\
id, kode, navn, opprettet_dato, sist_endret_dato, opprettet_av_bruker, sist_endret_av_bruker) \
VALUES ('{}', '{}', '{}', '2020-10-02 16:30:00.000000+00', '2020-10-02 16:30:00.000000+00', '00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000');\n".format(uuid.uuid1(), lineArray[0], lineArray[1])
    # print('insertScript: {}'.format(insertScript))

    return insertScript

if __name__ == '__main__':
    main()