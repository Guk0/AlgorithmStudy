# https://www.acmicpc.net/problem/2166
# 다각형의 면적
# 신발끈 공식

# https://coloredrabbit.tistory.com/164
# D = (x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1) / 2


n = STDIN.gets.chomp().to_i
arr = []
answer = [0, 0]

n.times do |_|
  arr.push(STDIN.gets.chomp().split(" ").map(&:to_i ))
end
arr.push(arr[0])

0.upto(arr.length-2) do |index|
  answer[0] += arr[index][0]*arr[index+1][1]
  answer[1] += arr[index][1]*arr[index+1][0]
end

puts ((answer[0]-answer[1]).abs.to_f/2).round(1)