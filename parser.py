import shutil
import shlex
s=[]
filter={'files':[],'exes':[],'url':[]}
delimiters=['|','&&',';','&']

with open('input.txt')as f:
    s+=f.readlines()

for i in s:
    d=[]
    cmd=shlex.split(i)[0]
    if(cmd not in filter['exes'] and cmd.isalpha()):
        filter['exes'].append(cmd)
    z=''
    x=shlex.split(i)
    for i,j in enumerate(x):
        if('://' in j):
            filter['url'].append(j)
            continue
        if('.'in j):
            if('/'in j):
                file=j[::-1][:j[::-1].index('/')][::-1]
            else:
                file=j
            if(not file[file.index('.')+1:].isalpha()):continue                
            if(file not in filter['files']):
                filter['files'].append(file)
        if(j in delimiters):
            d.append(i)
    try:
        for ind in d:
            if x[ind+1] not in filter['exes']:
                filter['exes'].append(x[ind+1])
    except:
        pass

for i in filter:
    print(i+":",filter[i])


print("\nCommands not installed:\n")
for i in filter['exes']:
    if(shutil.which(i)==None):
        print(i)



