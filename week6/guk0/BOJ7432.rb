# https://www.acmicpc.net/problem/7432
# 디스크트리
# trie


class Node
  attr_accessor :key, :data, :children
  def initialize(key, data=nil)
    @key = key
    @data = data
    @children = {}
  end
end

class Trie
  def initialize()
    @head = Node.new(nil)
  end

  def insert(texts)
    current_node = @head
    texts.each do |text|
      current_node.children[text] = Node.new(text) if current_node.children[text].nil?
      current_node = current_node.children[text]
    end
    current_node.data = texts
  end
  
  def solution(current_node, depth)
    current_node = @head if current_node.nil?
    $answer.push("#{" " * depth}#{current_node.key}") if depth >= 0
    if current_node.children.empty?
      return
    else
      current_node.children.each do |_, child_node|                
        solution(child_node, depth+1)
      end
    end
  end
end

N = STDIN.gets.chomp().to_i
trie = Trie.new()
arr = []
$answer = []

N.times do |_|
  arr.push(STDIN.gets.chomp().split("\\"))
end

arr.sort.each {|el| trie.insert(el) }

trie.solution(nil, -1)

puts $answer
# puts trie.inspect