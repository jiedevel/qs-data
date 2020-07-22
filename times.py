import subprocess
import json

url = "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2020_0__24cc3874b05eea134ee2716dbf93f11a.json"

cmd = 'curl'
cmds=[cmd, '-i', url]
tmp =subprocess.Popen(cmds, stdout=subprocess.PIPE)
outs = tmp.communicate()
print(type(outs))
for it in outs:
    print(type(it))
    if isinstance(it,bytes):
        string_it =  str(it, encoding='utf-8')
        #print(string_it)
        #jre = json.loads(string_it)
        #print(jre.keys)
        with open('res.txt','w') as f:
            f.write(string_it)

json_res =None
with open('res.txt','r') as f:
    count = 0
    for line in f.readlines():
        count = count +1
        if count == 24:
             json_res=json.loads(line)


print(json_res.keys())
print(type(json_res['data']))
print(json_res['data'][0].keys())
count=0
for it in json_res['data']:
    if it['location'] == 'Iran' and it['subjects_offered'].find('Physics') != -1:
        print('********')
        print(it['name'])
        for k, v in it.items():
            print('%s : %s' %(k,v))
        print('********')
        count = count +1

print('%s uni founded' %str(count))
