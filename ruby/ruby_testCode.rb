nations = ['한국', '일본', '베트남', '프랑스', '스페인']
capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}

nations.push('프랑스')

puts = nations

0.upto(2) do |x|
    puts nations[x]
end

nations.each do |x|
    puts x
end

capitals.each do |x, y|
    puts x, y
end
