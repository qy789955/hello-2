import pandas as pd
weight1 = 1
weight2 = 1
bias = 0.5

test_inputs = [(0,0),(0,1),(1,0),(1,1)]
correct_outputs = [False,True,True,True]
outputs = []

for test_input,correct_output in zip(test_inputs,correct_outputs):
    linear_combination = weight1*test_input[0] + weight2*test_input[1] - bias
    output = int(linear_combination >= 0)
    is_correct = "yes" if output == correct_output else "no"
    outputs.append([test_input[0],test_input[1],output,correct_output,is_correct]) # append()参数以列表的形式

output_frame = pd.DataFrame(outputs,columns=["Input1","Input2","outputs","correct_outputs","is correct"])
print(output_frame.to_string(index=False))
