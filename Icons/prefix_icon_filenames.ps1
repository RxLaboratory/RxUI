cd 10w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:w?\d*_)?(.+)','w10_$1'} -Force
cd ..
cd 14w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:w?\d*_)?(.+)','w14_$1'} -Force
cd ..
cd 18w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:w?\d*_)?(.+)','w18_$1'} -Force
cd ..
cd 25w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:w?\d*_)?(.+)','w25_$1'} -Force
cd ..
cd 32w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:w?\d*_)?(.+)','w32_$1'} -Force