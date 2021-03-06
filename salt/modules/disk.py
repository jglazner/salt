'''
Module for gathering disk information
'''

# FIXME: we want module internal calls rather than using subprocess directly
import subprocess


def usage():
    '''
    Return usage information for volumes mounted on this minion

    CLI Example::

        salt '*' disk.usage
    '''
    cmd = 'df -P'
    ret = {}
    out = subprocess.Popen(cmd,
            shell=True,
            stdout=subprocess.PIPE).communicate()[0].split('\n')
    for line in out:
        if not line.count(' '):
            continue
        if line.startswith('Filesystem'):
            continue
        comps = line.split()
        ret[comps[0]] = {
            '1K-blocks': comps[1],
            'available': comps[3],
            'capacity': comps[4],
            'mountpoint': comps[5],
            'used': comps[2]
        }
    return ret
