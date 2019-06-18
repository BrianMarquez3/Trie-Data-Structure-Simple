# Programa de Python para insertar y buscar.
# operation in a Trie 

class TrieNode: 
	
	# Trie clase node
	def __init__(self): 
		self.children = [None]*26

		# isEndOfWord es verdadero si el nodo representa el final de la palabra
		self.isEndOfWord = False

class Trie: 
	
	# Trie data clase estructura
	def __init__(self): 
		self.root = self.getNode() 

	def getNode(self): 
	
		# Devuelve un nuevo nodo trie (inicializado a NULL)
		return TrieNode() 

	def _charToIndex(self,ch): 
		
		# función auxiliar privada 
		# Convierte el personaje actual clave en índice
		# use solo 'a' a 'z' y minúscula
		
		return ord(ch)-ord('a') 


	def insert(self,key): 
		
		# Si no está presente, inserta la clave en trie 
		# Si la clave es el prefijo de trie node,
		# solo marca el nodo de la hoja
		pCrawl = self.root 
		length = len(key) 
		for level in range(length): 
			index = self._charToIndex(key[level]) 

			# si el caracter actual no esta presente
			if not pCrawl.children[index]: 
				pCrawl.children[index] = self.getNode() 
			pCrawl = pCrawl.children[index] 

		# marcar el último nodo como hoja
		pCrawl.isEndOfWord = True

	def search(self, key): 
		
		# Clave de búsqueda en el trie.
		# Devuelve true si presenta clave
		# en trie, sino falso
		pCrawl = self.root 
		length = len(key) 
		for level in range(length): 
			index = self._charToIndex(key[level]) 
			if not pCrawl.children[index]: 
				return False
			pCrawl = pCrawl.children[index] 

		return pCrawl != None and pCrawl.isEndOfWord 

# Manejo de Funcion
def main(): 

	# Teclas de entrada (use solo 'a' a 'z' y minúscula)
	keys = ["the","a","there","anaswe","any", 
			"by","their"] 
	output = ["Not present in trie", 
			"Present in trie"] 

	# Trie object 
	t = Trie() 

	# Construct trie 
	for key in keys: 
		t.insert(key) 

	# Search for different keys 
	print("{} ---- {}".format("the",output[t.search("the")])) 
	print("{} ---- {}".format("these",output[t.search("these")])) 
	print("{} ---- {}".format("their",output[t.search("their")])) 
	print("{} ---- {}".format("thaw",output[t.search("thaw")])) 

if __name__ == '__main__': 
	main() 


