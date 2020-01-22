
def levensthein_iterative(word_a: str, word_b: str, memory: list) -> int:
  """Calculates the Levensthein Distance
  (dynamically) between two strings.

  Parameters:
  word_a (str): The first word to be diffed.
  word_b (str): The second word to be diffed.

  Returns:
  int: The Levensthein Distance between word_a and word_b
  """
  # Check for empty words
  if not word_a: return len(word_b)
  if not word_b: return len(word_a)
  for col in range(1, len(word_b) + 1):
  # For every cost in word_a (insertions)
    for row in range(1, len(word_a) + 1):
      # For every cost in word_b (deletions)
      # If it's a substitution.
      if (word_a[row - 1] == word_b[col - 1]): cost = 0
      # Else, it's a insertion or deletion.
      else: cost = 1
      # The current edit distance will be the minimun between a deletion, insertion or substitution. 
      memory[row][col] = min(1 + memory[row - 1][col], 1 + memory[row][col - 1], cost + memory[row - 1][col - 1])
  return memory[len(word_a)][len(word_b)]

# MAIN PROCEDURE
def main():
  word_a = "HONDA"
  word_b = "HYUNDAI"
  matrix = initialize_matrix(len(word_a) + 1, len(word_b) + 1)
  for i in range(1, len(word_a) + 1):
    matrix[i][0] = i
  for j in range(1, len(word_b) + 1):
    matrix[0][j] = j

  # print(matrix)
  distance = levensthein_iterative(word_a, word_b, matrix)
  print(distance)

def initialize_matrix(n,m):  
  return [[0 for x in range(m)] for x in range(n)]

main()