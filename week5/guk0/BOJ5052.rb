# https://www.acmicpc.net/problem/5052
# 전화번호 목록
# trie


class Node
  attr_reader :key, :data, :children
  attr_writer :data, :children
  
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

  def insert(text)
    current_node = @head

    text.each_char do |char|
      current_node.children[char] = Node.new(char) if !current_node.children.include? char
      current_node = current_node.children[char]
    end
    current_node.data = text
  end

  def search(text)
    current_node = @head
    text.each_char do |char|
      current_node = current_node.children[char]
    end
    if current_node.children.empty?
      false # 접두사가 아니면
    else
      true # 접두사라면      
    end
  end
end
  

def check(arr, trie)
  arr.each do |el|
    if trie.search(el)
      return "NO"
    end
  end
  "YES"
end

t = STDIN.gets.chomp().to_i

t.times do |_|
  n = STDIN.gets.chomp().to_i
  arr = []
  trie = Trie.new()

  n.times do |_|
    text = STDIN.gets.chomp()
    trie.insert(text)
    arr.push(text)
  end

  arr.sort()
  puts check(arr, trie)
end
