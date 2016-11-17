import os
import shutil

## Files must have unique names or they will overwrite

RootDir1 = r'/volume1/4humwe1s-GDrive/we1s-3/data_archive/corpus/'
TargetFolder = r'/volume1/DockerData/dfrb/mount/read/metadata/'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith('.csv'):
                print "Copying "+name
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, TargetFolder) #copies csv to new folder

## NOTES:
## http://stackoverflow.com/questions/29685366/copy-files-from-multiple-directories-into-one-directory-using-python
