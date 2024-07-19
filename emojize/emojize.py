import emoji
user_ans = input("Input:")
find_em=user_ans.find(":")

emoji_name=user_ans[find_em:]
other=user_ans[:find_em]
create_em=emoji.emojize(emoji_name, language='alias')
print("Output:", other + create_em)