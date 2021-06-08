pairs = {'한국'=>'서울', '베트남'=>'하노이', '미국'=>'워싱턴'}

loop do
    pairs.each do |nation,  capital|
        puts nation + "의 수도를 맞추세요."

        answer = gets.chomp

        if answer == capital
            puts ''
            puts "◇◇◇◇ 정답 입니다 ◇◇◇◇"
            puts ''
            pairs.delete(nation)
        else
            puts '!!!!!!!!!!!오답 입니다!!!!!!!!!!!!'
            puts ''
            puts '====================='
            puts '정답은' + capital + '입니다.'
            puts '====================='
            puts ''
        end
    end
    if pairs.size == 0
        break
    end
    puts '모든 질문이 끝났습니다.' 
    puts '남은 오답이 다시 출제 됩니다.'
    puts ''
end