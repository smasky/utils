import os
import re
def deal_sectionPoints(Section_y,meter):
    num_min=Section_y.index(min(Section_y))
    list_min=[]
    list_min.append(num_min)
    for i in range(num_min+1,len(Section_y)):
        if(Section_y[num_min]==Section_y[i]):
            list_min.append(i)
        else:
            break
    print(list_min)
    for j in list_min:
        Section_y[j]=Section_y[j]-meter
    return Section_y
def write_SectionFile(lines,Section_x,Section_y):
    global new_lines
    new_lines+=lines
    num_min=Section_y.index(min(Section_y))
    left_Section=Section_y[0:num_min]
    right_Section=Section_y[num_min:]
    left_max=left_Section.index(max(left_Section))
    right_max=right_Section.index(max(right_Section))+num_min
    for i in range(len(Section_x)):
        if(i==num_min):
            string="{}    {}    1.000    {}    0    0.00    0\n".format(Section_x[i],Section_y[i],'<#2>')
        elif(i==left_max):
            string="{}    {}    1.000    {}    0    0.00    0\n".format(Section_x[i],Section_y[i],'<#1>')
        elif(i==right_max):
            string="{}    {}    1.000    {}    0    0.00    0\n".format(Section_x[i],Section_y[i],'<#4>')
        else:
            string="{}    {}    1.000    {}    0    0.00    0\n".format(Section_x[i],Section_y[i],'<#0>')

        new_lines.append(string)
    return new_lines


lines=[]
Section_x=[]
Section_y=[]
Section=[]
is_sectionPoints=False
new_lines=[]
with open('./123456.txt','r') as f:
    for line in f:
        string=str(line).strip('\n')

        if('LEVEL PARAMS' in string):
            Section=deal_sectionPoints(Section_y,1)
            new_lines=write_SectionFile(lines,Section_x,Section_y)
            lines=[]
            Section_x=[]
            Section_y=[]
            Section=[]
            is_sectionPoints=False


        if(is_sectionPoints):
            print(string)
            match=re.match(r"\s*([-0-9.]*)\s*([-0-9.]*)\s*",string)
            result=match.groups()
            Section_x.append(float(result[0]))
            Section_y.append(float(result[1]))
        else:
            lines.append(line)

        if('PROFILE' in string):
            is_sectionPoints=True

with open('rhsd-1.txt','w') as f:
    for lines in new_lines:
        f.write(lines)
