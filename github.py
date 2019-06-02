from subprocess import call
import config, time

def commit():
	cwd = config.CHROME['downloads']
	call(['git', 'add', '.'], cwd=cwd)
	print("wait for 30 seconds to stage the changes")
	time.sleep(30)
	call(['git', 'commit', '-m', 'updating files'], cwd=cwd)
	print("wait for 30 seconds to commit the changes")
	time.sleep(30)
	call(['git', 'push', 'origin', 'master'], cwd=cwd)
