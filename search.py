if __name__== "__main__":
    movies_list = ["Avenger Endgame","Avenger Infinity War","The Avengers","Iron Man 3"]
user = input("Enter Movie name:")
search_list = []
index = 0

split_user = user.split(" ")

    for movies in movies_list:
        index += 1
        split = movies.split(" ")
        for keyboard1 in split_user:
           for keyboard2 in split_moviesList:
               if keyboard1.lower() == keyboard2.lower():
                  search_list.append(index)
                  
print(len(search_list),"Results found\")
for index in search_list:
    print(movies_list[index-1]+"\n")
    
