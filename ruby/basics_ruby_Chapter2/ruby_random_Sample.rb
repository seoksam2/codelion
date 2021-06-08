# import random

# list = ["한국", "베트남", "미국"]
# result = random.sample(list, 1)

# print(result)

puts ['한국', '베트남', '미국', '프랑스', '스페인'].sample


1.upto(10) do
    puts ['한국', '베트남', '미국', '프랑스', '스페인'].sample
end


10.downto(1) do
    puts ['한국', '베트남', '미국', '프랑스', '스페인'].sample
end


loop do
    puts ['한국', '베트남', '미국', '프랑스', '스페인'].sample
    break
end
