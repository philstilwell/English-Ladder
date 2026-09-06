"""Carry only new source data across a workflow retry, never stale HTML."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def digest(data):return hashlib.sha256(data).hexdigest() if data is not None else None

def tracked_version(path):
    result=subprocess.run(['git','show','HEAD:'+path],cwd=ROOT,capture_output=True)
    return result.stdout if result.returncode==0 else None

def allowed(path):
    p=Path(path)
    return not p.is_absolute() and '..' not in p.parts and (path.startswith('archive/lessons/') or path.startswith('assets/news/'))

def capture(destination):
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True);manifest=[]
    for folder in ['archive/lessons','assets/news']:
        for file in sorted((ROOT/folder).rglob('*')):
            if not file.is_file():continue
            name=file.relative_to(ROOT).as_posix();data=file.read_bytes();baseline=tracked_version(name)
            if data==baseline:continue
            target=destination/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
            manifest.append({'path':name,'baseline':digest(baseline),'incoming':digest(data)})
    (destination/'manifest.json').write_text(json.dumps(manifest))
    print(f'Saved {len(manifest)} changed source-data files for publication.')

def restore(destination):
    destination=Path(destination);manifest=json.loads((destination/'manifest.json').read_text());writes=[]
    for item in manifest:
        name=item['path']
        if not allowed(name):raise ValueError('Invalid source-data path in publication snapshot.')
        file=ROOT/name;data=(destination/name).read_bytes()
        if digest(data)!=item['incoming']:raise ValueError('Damaged publication snapshot: '+name)
        current=digest(file.read_bytes() if file.exists() else None)
        if current not in [item['baseline'],item['incoming']]:
            raise RuntimeError('Concurrent source edit requires review; refusing to overwrite '+name)
        writes.append((file,data))
    for file,data in writes:file.parent.mkdir(parents=True,exist_ok=True);file.write_bytes(data)
    print('Restored source data; public pages must now be rebuilt with the current templates.')

if __name__=='__main__':
    {'capture':capture,'restore':restore}[sys.argv[1]](sys.argv[2])
