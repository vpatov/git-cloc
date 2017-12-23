import subprocess
import re
import random
import os
import json

"""
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
"""


gitdir = "/home/vasia/repos/522/"
commit_pattern = re.compile(r'[\da-f]{40}')
#date_pattern = re.compile(r'(%s){1}\s(%s){1}\s\d{1,2}\s' % ('|'.join(days),'|'.join(months)))
#date_pattern = re.compile(r'Date:\s+[a-zA-Z]{3}\s[a-zA-Z]{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4}')
"""
gitremote_out = subprocess.run(["git remote"],cwd=gitdir,shell=True,stdout=subprocess.PIPE)
gitremote = gitremote_out.stdout.decode()

gitremote_geturl_out = subprocess.run(["git remote get-url %s" % (gitremote)],cwd=gitdir,shell=True,stdout=subprocess.PIPE)
gitremote_url = gitremote_geturl_out.stdout.decode()
"""

tmpnum = random.randint(1000000,10000000)
tmpdir = '/tmp/%d' % (tmpnum)
while (os.path.exists(tmpdir)):
	tmpdir = '/tmp/%d' % (random.randint(1000000,10000000))
os.mkdir(tmpdir)

subprocess.run(["cp -r . %s" % (tmpdir)],cwd=gitdir,shell=True)

gitlog_out = subprocess.run(["git log"],cwd=tmpdir,shell=True,stdout=subprocess.PIPE)
commits = commit_pattern.findall(gitlog_out.stdout.decode())

##git log -1 --format=%cd

devnull = open(os.devnull, 'wb')

subprocess.run(["git add ."],cwd=tmpdir,shell=True,stdout=devnull,stderr=devnull)
subprocess.run(["git commit -m \"gitcloc temp commit %d\"" % (tmpnum)],cwd=tmpdir,shell=True,stdout=devnull,stderr=devnull)
for commit in commits:
	subprocess.run(["git checkout %s" % (commit)],shell=True,cwd=tmpdir,stdout=devnull,stderr=devnull)
	commit_date_out = subprocess.run(["git log -1 --format=%cd"],shell=True,cwd=tmpdir,stdout=subprocess.PIPE)
	commit_date = ' '.join(commit_date_out.stdout.decode().split(' ')[:-1])
	print("Commit: %s... %s" % (commit[0:8], commit_date))
	cloc_out = subprocess.run(["cloc . --json"],shell=True,cwd=tmpdir,stdout=subprocess.PIPE)
	cloc_dict = json.loads(cloc_out.stdout.decode())
	for code_type in cloc_dict:
		if code_type == 'header':			
			continue
	
		print("\033[1;36m" "%s: %s" "\033[0m" % (code_type,cloc_dict[code_type]["code"]))
	print()
