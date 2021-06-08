puts '참여할 인원의 이름을 모두 적어주세요. 구분은 빈칸으로 합니다.'
people = gets.chomp.split(" ")

puts '며칠 간 진행 합니까?'
days = gets.chomp.to_i #문자를 숫자로 변경

@meeting = {}

1.upto(days) do |day|
    @meeting[day] = [] 
end

people.each do |person|
    1.upto(days) do |day|
        puts person +'님은 '+ day.to_s + '일에 참석 가능하신가요? (Y/y)'
        answer = gets.chomp
        if  answer.downcase == 'y' # answer의 입력 값을 소문자로 변경
            @meeting[day]<<person
        end
    end
end    

def print_meeting
    @meeting.each do |day, person|
        puts day.to_s+" "+person.to_s
    end
end

print_meeting

