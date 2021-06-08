capitals = {'한국' => '서울', '베트남' => '하노이', '미국' => 
'워싱턴', '스페인'=>'마드리드'}

capitals['프랑스'] = '파리'
capitals.delete('미국')

puts capitals.size
puts capitals.invert
puts capitals
puts capitals['한국']

# nations = ['한국', '베트남', '파리']

# puts nations.first
# puts nations.last
# nations.push("인도")
# nations.delete("파리")
# puts nations
