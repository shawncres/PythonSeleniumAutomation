##Script to initiate folder stucture 


folderStruct = {'AutomationFramework': {'Hivemind': ['TestCases', 'Data']}}


os.makedirs(r'C:\Users\ShawnCooper\OneDrive - ATTAbotics\Desktop\Test\Framework\Misc',exist_ok=False)


os.removedirs(r'C:\Users\ShawnCooper\OneDrive - ATTAbotics\Desktop\test\Framework\Misc')



folderStruct['AutomationFramework']['Hivemind']

for i in folderStruct.keys():
    print(i)

for i in folderStruct.keys():
    print(r'C:\\'+i)
