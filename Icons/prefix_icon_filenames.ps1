cd 10w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:\d*_)?(.+)','w10_$1'}
cd ..
cd 14w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:\d*_)?(.+)','w14_$1'}
cd ..
cd 18w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:\d*_)?(.+)','w18_$1'}
cd ..
cd 25w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:\d*_)?(.+)','w25_$1'}
cd ..
cd 32w
Get-ChildItem *.png | rename-item -NewName {$_.name -Replace '^(?:\d*_)?(.+)','w32_$1'}