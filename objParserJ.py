#!/usr/bin/python
import os
import sys

def parseVertices(content):
    unique_verts = []
    for line in content:
        if line[0] == 'v' and line[1] != 'n':
            vert_line = line[2:]
            unique_verts.append(vert_line.replace('\n', '').split(' '))
    return unique_verts

def parseNormals(content):
    unique_norms = []
    for line in content:
        if line[0] == 'v' and line[1] == 'n':
            normals_line = line[3:]
            unique_norms.append(normals_line.replace('\n', '').split(' '))
    return unique_norms


def treat_indices(content):
    for line in content:
        if line[0] == 'f':
            indices_line = line[2:]
            indGroup = []

            # I'm very sorry for the next +/- 10 lines.
            # Actually +/- 15 lines.
            for i in range(3):
                startInd = 0
                endInd = 0
                for ind in range(indices_line.__len__()):
                    if indices_line[ind+1] == '/':
                        endInd = ind
                        break
                uniqueVertInd = int(indices_line[startInd:endInd+1]) - 1
                startInd = endInd + 3
                for ind in range(indices_line.__len__()):
                    if ind+1 == indices_line.__len__() or indices_line[ind+1] == ' ':
                        endInd = ind
                        break
                uniqueNormInd = int(indices_line[startInd:endInd+1]) - 1
                print str(uniqueVertInd) + "//" + str(uniqueNormInd)
                indices_line = indices_line[endInd+1:]
                foundInd = False
                #if vert/norm exists, use its index
                for pointInd in range(vertices.__len__()):
                    if vertices[pointInd] == unique_vertices[uniqueVertInd]:
                        if normals[pointInd] == unique_normals[uniqueNormInd]:
                            indGroup.append(pointInd + 1) #1-based
                            foundInd = True
               #else create new vert/norm, use its index
                if foundInd == False:
                    vertices.append(unique_vertices[uniqueVertInd])
                    normals.append(unique_normals[uniqueNormInd])
                    indGroup.append(vertices.__len__()) #1-based
            indices.append(indGroup)            

    #function to write in the file the verts/indices/normals
def write_list(list, count, file):
    for i in range(list.__len__()): #write the vector in groups of 3 separated by comma
        for v in range((list[i]).__len__()):           # and separate verts, normals, indices by ;
            if(v != (list[i]).__len__() -1 ):
                file.write(str(list[i][v]) + ' ')
            else:
                file.write(str(list[i][v]))
        if(i != list.__len__()- 1):
            file.write(',')
        elif(count != 3):   #if it is not the last list (indices) to write dont put ';'' else put ;
            file.write(';')

if __name__ == "__main__":
    name = sys.argv[1]
    final_file = open(name.replace('.obj','.txt'), 'a+')
    with open(name, 'r') as f:
        content = f.readlines()
        unique_vertices = parseVertices(content)
        unique_normals = parseNormals(content)

        vertices = []
        normals = []
        indices = []

        treat_indices(content)

        write_list(vertices, 1, final_file)
        write_list(normals, 2, final_file)
        write_list(indices, 3, final_file)
