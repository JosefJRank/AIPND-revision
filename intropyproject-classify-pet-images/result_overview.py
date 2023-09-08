# PROGRAMMER: Josef Rank    
# DATE CREATED: 11.08.2023                                
# REVISED DATE: 
# PURPOSE: This script creates an overview of the listed result files of the check_images.py script.


def parse_result_file(FileName):        
    result_list = []
    with open(FileName) as f:       
        for line in f:
            print(line)
            if ('#' in line) & (':' in line):
                model = line.split(':')[1].split('#')[0].strip()
                continue
            if ('*' in line) & (':' in line):#Find the lines with result values
                fractured_line = line.split(':')
                fractured_line = line.split(' ')                
                linepart_number = 0
                for linepart in fractured_line[1:]: # Find the the result values in the lines
                    linepart_number +=1
                    if linepart == ':':
                        result_list.append(fractured_line[linepart_number+1].split('\n')[0])
            if ('Total Elapsed Runtime' in line):
                result_list.append(linepart.strip())


    return model, result_list

ResultFile_List = ['alexnet_pet-images.txt','resnet_pet-images.txt','vgg_pet-images.txt']
Result_List = []
for ResultFile in ResultFile_List:
    model, result = parse_result_file(ResultFile)
    print(model)
    print(result)
    Result_List.append([model,result])

with open('check_images_result.txt','w') as Result_File:
    line = '...'
    Result_File.write('################################################################################################')
    Result_File.write('\n')
    Result_File.write('# This is the Result of the comparison of alexnet, resnet and vpp for dog image classification #')
    Result_File.write('\n')
    Result_File.write('################################################################################################')
    Result_File.write('\n')
    Result_File.write('\n')
    Result_File.write('\n')
    Result_File.write('Total Images: {}\n'.format(Result_List[0][1][0]))
    Result_File.write('Dog Images: {}\n'.format(Result_List[0][1][1]))
    Result_File.write('Not-a-Dog Images: {}\n'.format(Result_List[0][1][2]))
    Result_File.write('\n')
    Result_File.write('{:<30s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} \n'.format('CNN Model Architecture:','Not-a-Dog','Dogs', 'Breeds', 'Match', 'Processing Time'))
    Result_File.write('{:<30s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} \n'.format(' ','Correct','Correct', 'Correct', 'Labels',' '))
    Result_File.write('----------------------------------------------------------------------------------------------------\n')
    Result_File.write('{:<30s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} \n'.format((Result_List[0][0]),(Result_List[0][1][5]),(Result_List[0][1][4]), (Result_List[0][1][6]), (Result_List[0][1][7]), (Result_List[0][1][10])))
    Result_File.write('{:<30s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} \n'.format((Result_List[1][0]),(Result_List[1][1][5]),(Result_List[1][1][4]), (Result_List[1][1][6]), (Result_List[1][1][7]), (Result_List[1][1][10])))
    Result_File.write('{:<30s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} \n'.format((Result_List[2][0]),(Result_List[2][1][5]),(Result_List[2][1][4]), (Result_List[2][1][6]), (Result_List[2][1][7]), (Result_List[2][1][10])))


