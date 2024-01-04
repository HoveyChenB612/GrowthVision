import ast
import json
# 字符串包含一个字面值表达式
string_with_literal = "[1, 2, 3.0 ,'asd', 'wef','qweasd''123']"

# 使用 ast.literal_eval 解析字符串
parsed_list = ast.literal_eval(string_with_literal)


print(parsed_list)
print(type(parsed_list))

l1 = [1, 2, 3.0, 'asd', 'wef', 'qweasd123']

parsed_str = json.dumps(l1)
print(parsed_str)
print(type(parsed_str))