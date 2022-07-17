# https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=ruby
# 영어 끝말잇기

require "set"

def solution(n, words)
    answer = []
    index = 0
    used = Set.new([words[0]])
    
    while true      
        index += 1
        if index == words.length
            break
        end
                
        if !used.include?(words[index]) && words[index][0] == words[index-1][-1]
            used.add(words[index])
        else
            return [index % n + 1, index / n + 1]
        end
    end
    
    return [0, 0]
end