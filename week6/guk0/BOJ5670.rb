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

  def insert(text)
    current_node = @head

    text.each_char do |char|
      current_node.children[char] = Node.new(char) if current_node.children[char].nil?
      current_node = current_node.children[char]
    end

    current_node.data = text
  end

  def search(node, cnt)
    node = @head if node.nil?
    if !node.data.nil?
      $total_pressed += cnt
      return if node.children.empty?
    end

    if node.children.length.eql?(1) && !node.key.nil? && node.data.nil?
      search_children(node, cnt)
    else
      search_children(node, cnt+1)
    end
  end

  private
  def search_children(node, cnt)
    node.children.each do |_, child_node|
      search(child_node, cnt)
    end
  end
end


while true
  n = STDIN.gets.chomp()
  break if n.eql?("")
  trie = Trie.new
  arr = []
  n.to_i.times do |_|
    arr.push(STDIN.gets.chomp())
  end
  arr.sort.each {|el| trie.insert(el) }
  $total_pressed = 0
  trie.search(nil, 0)

  puts("%.2f" % ($total_pressed.to_f / n.to_i))
end



# def search(node, cnt)
#   node = @head if node.nil?
#   if node.children.empty?
#     $total_pressed += cnt
#     p $total_pressed
#     return
#   end
#   # p cnt
#   $total_pressed += cnt if !node.data.nil?
#   p $total_pressed if !node.data.nil?
#   node.children.each do |_, child_node|
#     # data있고 children 여러개 vs data 있고 children 한개
#     search(child_node, node.children.length.eql?(1) && node.data.nil? ? cnt : cnt+1)
#   end
# end


# hello 3
# hell  2
# heaven  2
# goodbye 1

# 5
# hi 1 
# he 1 
# h  