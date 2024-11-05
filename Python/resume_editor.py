'''
Working on a way to parse my resume automatically
and add/remove/edit items easier.
'''

def getResumeLines(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()

    return lines

def getProjects(lines):
    projects = {}
    pass

