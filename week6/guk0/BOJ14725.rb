# https://www.acmicpc.net/problem/14725
# 개미굴
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
      current_node.children[text] = Node.new(text) if !current_node.children.include? text
      current_node = current_node.children[text]
    end
    current_node.data = texts
  end

  def solution(current_node, depth)
    current_node = @head if current_node.nil?

    $answer.append("#{"-"* depth *2}#{current_node.key}") if !current_node.key.nil?
    if current_node.children.empty?
      return
    else
      current_node.children.each do |_, value|
        self.solution(value, depth+1)
      end
    end
  end
end

N = STDIN.gets.chomp().to_i
arr = []
trie = Trie.new()
$answer = []

N.times do |_|
  texts = STDIN.gets.chomp().split(" ")[1..-1]
  arr.append(texts)  
end

arr.sort!
arr.each do |texts|
  trie.insert(texts)
end

trie.solution(nil, -1)


puts $answer