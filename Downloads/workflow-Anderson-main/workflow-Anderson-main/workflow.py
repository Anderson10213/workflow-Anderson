import os, subprocess, datetime, random
for i in range(528):
    dt = datetime.datetime(2022, 1, 13) + datetime.timedelta(seconds=random.randint(0, 4*365*86400))
    date_str = dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')
    open('log.txt', 'a').write(f'commit {i}\n')
    subprocess.run(['git', 'add', '.'])
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    subprocess.run(['git', 'commit', '-m', f'auto: update {i}'], env=env)